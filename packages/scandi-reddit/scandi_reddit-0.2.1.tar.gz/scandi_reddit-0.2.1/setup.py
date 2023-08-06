# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['scandi_reddit']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=2.7.1,<3.0.0',
 'datasketch>=1.5.8,<2.0.0',
 'luga>=0.2.6,<0.3.0',
 'more-itertools>=9.0.0,<10.0.0',
 'nlp-dedup>=0.1.1,<0.2.0',
 'pandas>=1.5.2,<2.0.0',
 'wget>=3.2,<4.0',
 'zstandard>=0.19.0,<0.20.0']

entry_points = \
{'console_scripts': ['build = scandi_reddit.cli:main']}

setup_kwargs = {
    'name': 'scandi-reddit',
    'version': '0.2.1',
    'description': 'Construction of a Scandinavian Reddit dataset.',
    'long_description': '# ScandiReddit\n\nConstruction of a Scandinavian Reddit dataset.\n\n______________________________________________________________________\n[![Documentation](https://img.shields.io/badge/docs-passing-green)](https://alexandrainst.github.io/ScandiReddit/scandi_reddit.html)\n[![License](https://img.shields.io/github/license/alexandrainst/ScandiReddit)](https://github.com/alexandrainst/ScandiReddit/blob/main/LICENSE)\n[![LastCommit](https://img.shields.io/github/last-commit/alexandrainst/ScandiReddit)](https://github.com/alexandrainst/ScandiReddit/commits/main)\n[![Code Coverage](https://img.shields.io/badge/Coverage-0%25-red.svg)](https://github.com/alexandrainst/ScandiReddit/tree/main/tests)\n\n\nDevelopers:\n\n- Dan Saattrup Nielsen (dan.nielsen@alexandra.dk)\n\n\n# Installation\n\nThe package is available on PyPI, so you can install the package using your favourite\npackage manager. For instance, `pip install scandi_reddit` or `poetry add\nscandi_reddit`.\n\n\n# Quick start\n\nSimply run the command `build` in the terminal to build the dataset. This takes quite a\nwhile! See `$ build --help` for more information on all the settings.\n',
    'author': 'Dan Saattrup Nielsen',
    'author_email': 'dan.nielsen@alexandra.dk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
