# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metropro_dat_reader']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mpdr = metropro_dat_reader.main:app']}

setup_kwargs = {
    'name': 'metropro-dat-reader',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Riley Shea',
    'author_email': 'riley.shea@liftbridgesw.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
