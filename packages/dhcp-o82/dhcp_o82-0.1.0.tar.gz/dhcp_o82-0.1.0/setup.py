# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dhcp_o82']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'netaddr>=0.8.0,<0.9.0']

entry_points = \
{'console_scripts': ['dhcp-o82 = dhcp_o82.cli:cli']}

setup_kwargs = {
    'name': 'dhcp-o82',
    'version': '0.1.0',
    'description': 'Makes humans working with DHCP Option 82/RelayAgentInfo possible.',
    'long_description': None,
    'author': 'Manny Garcia',
    'author_email': 'mannygar@cisco.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
