# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['next_composer_vault']

package_data = \
{'': ['*']}

install_requires = \
['hvac==0.11.2']

setup_kwargs = {
    'name': 'next-composer-vault',
    'version': '0.1.0',
    'description': '',
    'long_description': 'poetry config pypi-token.pyp TOKEN\n',
    'author': 'Victor Tsetsulin',
    'author_email': 'victor.tsetsulin@nexttrucking.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
