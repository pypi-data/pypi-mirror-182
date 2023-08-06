# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['txsweeper']

package_data = \
{'': ['*']}

install_requires = \
['textual>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['txSweeper = txSweeper.main:main']}

setup_kwargs = {
    'name': 'txsweeper',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'k01e',
    'author_email': 'k01e.alm07@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
