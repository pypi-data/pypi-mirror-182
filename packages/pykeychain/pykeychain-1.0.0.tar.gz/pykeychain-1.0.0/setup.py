# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pykeychain']

package_data = \
{'': ['*']}

install_requires = \
['sh>=1.14.3,<2.0.0']

setup_kwargs = {
    'name': 'pykeychain',
    'version': '1.0.0',
    'description': 'Library for adding, getting and removing simple passwords from macos keychain.',
    'long_description': '# pykeychain\n\n[![Python package](https://github.com/elisey/pykeychain/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/elisey/pykeychain/actions/workflows/python-package.yml)\n\nLibrary for adding, getting and removing simple passwords from macos keychain.',
    'author': 'Elisei',
    'author_email': 'elisey.rav@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/elisey/pykeychain',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
