# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['playhdl', 'playhdl.templates']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['playhdl = playhdl.cli:main']}

setup_kwargs = {
    'name': 'playhdl',
    'version': '0.1.0',
    'description': 'Tool to play with HDL (inspired by EdaPlayground)',
    'long_description': None,
    'author': 'esynr3z',
    'author_email': 'esynr3z@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
