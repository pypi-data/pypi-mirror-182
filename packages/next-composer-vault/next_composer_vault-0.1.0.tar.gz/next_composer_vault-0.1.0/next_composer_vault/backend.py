from airflow.secrets import BaseSecretsBackend
from next_composer_vault.client import get_secret


class NextVaultSecretBackend(BaseSecretsBackend):
    def get_variable(self, key):
        from airflow.models import Variable
        val = get_secret(key, "variables")
        return Variable(key=key, val=val)

    def get_connection(self, conn_id):
        from airflow.models import Connection
        secret = get_secret(conn_id, "connections")
        conn = Connection(
            conn_id=conn_id,
            conn_type=secret.get('Type'),
            description=secret.get('Description'),
            host=secret.get('Host'),
            login=secret.get('Login'),
            password=secret.get('Password'),
            schema=secret.get('Schema'),
            port=secret.get('Port'),
            extra=secret.get('extra'),
            uri=secret.get('URI'))
        return conn
