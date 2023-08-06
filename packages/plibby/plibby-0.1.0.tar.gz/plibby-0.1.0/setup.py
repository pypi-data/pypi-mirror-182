# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plibby']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'httpx>=0.23.1,<0.24.0',
 'loguru>=0.6.0,<0.7.0',
 'peewee>=3.15.4,<4.0.0',
 'rich>=12.6.0,<13.0.0',
 'zstandard>=0.19.0,<0.20.0']

setup_kwargs = {
    'name': 'plibby',
    'version': '0.1.0',
    'description': '',
    'long_description': "# plibby\n\nThis is an utils library for Python, which contains some useful functions. It's meant primarily\nfor my own use, but I'm sharing it in case it's useful to anyone else.\n",
    'author': 'Pedro Batista',
    'author_email': 'pedrovhb@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
