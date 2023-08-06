# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'gen'}

packages = \
['uhubspot',
 'uhubspot.components',
 'uhubspot.components.schemas',
 'uhubspot.paths',
 'uhubspot.paths.batchGetAssociations',
 'uhubspot.paths.getAssociations']

package_data = \
{'': ['*']}

install_requires = \
['lapidary>=0.7.3,<0.8.0']

setup_kwargs = {
    'name': 'hubspot-unofficial',
    'version': '0.1.0',
    'description': 'Reverse-engineered HubSpot client',
    'long_description': 'None',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
