import google.auth.transport.requests
import google.oauth2.id_token
import hvac
import os
import logging
import sqlite3
import time
from threading import Lock
from tenacity import retry, stop_after_delay, wait_random_exponential
import json


VAULT_ADDR = os.environ.get('VAULT_ADDR')
VAULT_ROLE = os.environ.get('VAULT_ROLE')

SECRET_TTL_SECONDS = 600
_SECRET_NOT_FOUND_SENTINEL = "<SECRET KEY NOT FOUND>"

# Module "global" vars.  Any more of these and we should start thinking if
# the logic in this file is better suited as a singleton class.
_vault_client = None
_vault_client_expiration_time = 0
_vault_client_lock = Lock()


def _get_vault_client():
    global _vault_client
    global _vault_client_expiration_time

    if _vault_client_expiration_time < time.time():
        auth_req = google.auth.transport.requests.Request()
        token = google.oauth2.id_token.fetch_id_token(
            auth_req, f"vault/{VAULT_ROLE}")

        _vault_client = hvac.Client(url=VAULT_ADDR)
        auth_info = _vault_client.auth.gcp.login(
            role=VAULT_ROLE,
            jwt=token
        )

        lease_duration_sec = auth_info['auth']['lease_duration']

        # Set the expiration 5 seconds before the lease expires
        _vault_client_expiration_time = int(
            time.time()) + ((lease_duration_sec - 5) * 60)
    return _vault_client


def get_secret(secret_id: str, secret_type: str) -> str:
    """
    We cache results for `SECRET_TTL` seconds to avoid calling vault (and by extension dynamodb) too frequently.
    """
    cache_key = f'{secret_type}/{secret_id}'
    logging.debug("Looking for secret: '{}'".format(cache_key))

    secret = None

    if not secret:
        secret = _get_secret_from_cache(cache_key, SECRET_TTL_SECONDS)

    # Still looking for the secret. Check in Vault
    if not secret:
        secret = _get_secret_from_vault(secret_id, secret_type)

    _cache_secret(cache_key, secret)

    if not secret or secret == _SECRET_NOT_FOUND_SENTINEL:
        raise KeyError(
            "Did not find secret for secret_id: '{}'".format(cache_key))

    return secret

# Cache the current value of `secret`. This is required as Airflow runs scripts in separate processes
# and therefore we cannot cache in process. We need to cache because Airflow re-"parses"
# the dags frequently.
#
# We also don't really care about race conditions here (e.g. multiple dags looking up the same value concurrently).
# All we want is to reduce the overall load on vault+dynamodb.  Depending on how much or little this helps,
# and how much dynamodb ends up costing to back vault, we may decide to remove this cache (since I [Kevin] _hate_ caching).


def _get_secret_from_cache(cache_key: str, ttl_seconds: str) -> str:
    conn = _get_conn()

    secret = None

    try:
        # next try to grab the secret from the "cache"
        logging.debug(
            "Checking for cached secret with name: '{}'".format(cache_key))

        cursor = conn.cursor()
        cursor.execute('SELECT secret, timestamp FROM secrets WHERE id = :id', {
                       "id": cache_key})
        dbResult = cursor.fetchone()

        if dbResult:
            insert_time = dbResult[1]

            time_diff = int(time.time()) - int(insert_time)
            logging.debug("Found cached var with timestamp: '{}', time diff: '{}'".format(
                insert_time, time_diff))

            # Use the secret if the ENV var was set within the secret's TTL
            if time_diff <= ttl_seconds:
                logging.debug(
                    "Cached secret is NOT expired. Using found value.")
                try:
                    secret = json.loads(dbResult[0])
                except ValueError:
                    secret = dbResult[0]
    except KeyError as e:
        logging.warn(
            "KeyError checking for secret: '{}' in the cache. Error: {}".format(cache_key, e))
    finally:
        conn.close()

    return secret


def _cache_secret(cache_key: str, secret: str) -> None:
    conn = _get_conn()
    try:
        cursor = conn.cursor()
        # The build in version of sqlite does not support the newer ON CONFLICT clause, so use INSERT OR REPLACE instead.
        cursor.execute("INSERT OR REPLACE INTO secrets (id, secret, timestamp) VALUES (:id, :secret, :timestamp)",
                       {"id": cache_key, "secret": json.dumps(
                           secret), "timestamp": int(time.time())}
                       )
        conn.commit()
    finally:
        conn.close()

# Check for secret in Vault.  Sometimes auth checks with Vault fail,
# and to cover any other transient lookup failures, we add `@retry` config to
# attempt recovery.


@retry(stop=stop_after_delay(90), wait=wait_random_exponential(max=15))
def _get_secret_from_vault(secret_id: str, secret_type: str) -> str:
    try:
        if secret_type == 'variables':  # variable are generic k/v types in airflow
            path = "composer/variables"
            key = secret_id
        elif secret_type == 'connections':  # connections are jsons
            path = f"composer/connections/{secret_id}"
            key = ''

        # The vault client uses the `requests` library and
        # appears to share the request's `session` object, which is
        # not thread safe. So we use a lock here just in case.
        global _vault_client_lock
        with _vault_client_lock:
            client = _get_vault_client()

        if client is None:
            return None

        secret = None
        secret_data = client.secrets.kv.v2.read_secret_version(path)

        if "data" in secret_data and "data" in secret_data["data"]:
            if key:
                secret = secret_data["data"]["data"].get(key)
            else:
                secret = secret_data["data"]["data"]
        if not secret:
            # This allows us to cache the result if the key does not exist in Vault or has no value.
            # In this case we've successfully received a response from Vault and not some other
            # issue with Vault itself, the network, etc (although these are likely to produce an Exception).
            # This is helpful to avoid spamming Vault if a key does not exist
            # in a particular environment.
            secret = _SECRET_NOT_FOUND_SENTINEL

            logging.warn(
                "Key: '{}' does not exist at path: '{}'".format(key, path))
    except hvac.exceptions.InvalidPath:
        logging.warn("InvalidPath: " + path, exc_info=True)
        # Cache not found result when path is invalid.
        secret = _SECRET_NOT_FOUND_SENTINEL
    except Exception:
        logging.exception(
            "Error fetching secret from Vault: '{}'".format(secret_id))
        raise

    return secret


def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect("/tmp/airflow-cache.db")
    _init_db(conn)

    return conn


def _init_db(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS secrets (id TEXT PRIMARY KEY, secret TEXT, timestamp INTEGER)')
    conn.commit()
