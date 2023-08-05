# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['custom_nmt']

package_data = \
{'': ['*']}

install_requires = \
['tensorflow>=2.11.0,<3.0.0']

setup_kwargs = {
    'name': 'custom-nmt',
    'version': '0.1.3',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
