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
    'version': '0.1.1',
    'description': 'CLI utility to read metropro dat files',
    'long_description': '# Metropro dat reader\n\n## Requirements\n\nPython 3.10 or higher https://www.python.org/downloads/\n\n## Install\n\nFrom the command line:\n\n`pip install metropro-dat-reader`\n\n## Usage\n\n`mpdr <path to dat file>`\n\nexamples:\n\n`mpdr C:\\Users\\user\\Downloads\\abc123.dat`\n\n`mpdr def456.dat`\n\n### Example output\n\n```text\n❮ mpdr SN9_PLANO_SR_UC37.dat\nSN9_PLANO_SR_UC37.dat\nmagic_number: 2283471727\nheader_format: 1\nheader_size: 834\nswinfo.type: 0\nswinfo.date:\nswinfo.vers.maj: 8\nswinfo.vers.min: 0\nswinfo.vers.bug: 0\n...\n```\n\n## Development setup\n\nTODO\n',
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
