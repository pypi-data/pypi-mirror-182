# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['harbor_client',
 'harbor_client.api',
 'harbor_client.harbor_client',
 'harbor_client.models']

package_data = \
{'': ['*']}

install_requires = \
['certifi>=14.05.14,<15.0.0',
 'python_dateutil>=2.5.3,<3.0.0',
 'setuptools>=21.0.0,<22.0.0',
 'six>=1.10,<2.0',
 'urllib3>=1.15.1,<2.0.0']

setup_kwargs = {
    'name': 'harbor-api-client',
    'version': '2.7.0',
    'description': 'Client for the Harbor API',
    'long_description': 'None',
    'author': 'Vadim Bauer',
    'author_email': 'vb@container-registry.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://container-registry.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
