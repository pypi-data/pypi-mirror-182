# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dumcure']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'dumcure',
    'version': '0.1.0',
    'description': 'Simple package which displays current currencies.',
    'long_description': '# Simple testing package, do not use',
    'author': 'buzonek',
    'author_email': 'buzonekk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
