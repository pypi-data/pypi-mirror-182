# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boltz_client']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'embit>=0.6.1,<0.7.0',
 'httpx>=0.23.1,<0.24.0',
 'websockets>=10.4,<11.0']

entry_points = \
{'console_scripts': ['boltz = boltz_client.cli:main']}

setup_kwargs = {
    'name': 'boltz-client',
    'version': '0.0.1',
    'description': 'python boltz client',
    'long_description': 'None',
    'author': 'dni',
    'author_email': 'office@dnilabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
