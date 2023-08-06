# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gwapandas', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.7.0,<0.8.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.4.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=4.0.3,<5.0.0',
         'mkdocs-material>=8.5.11,<9.0.0',
         'mkdocs-autorefs>=0.4.1,<0.5.0',
         'mkdocstrings[python]>=0.19.1,<0.20.0'],
 'test': ['black>=22.3.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

entry_points = \
{'console_scripts': ['gwapandas = gwapandas.cli:app']}

setup_kwargs = {
    'name': 'gwapandas',
    'version': '0.0.2',
    'description': 'Python tools for GWAS summary statistics.',
    'long_description': '# gwapandas\n\n\n[![pypi](https://img.shields.io/pypi/v/gwapandas.svg)](https://pypi.org/project/gwapandas/)\n[![python](https://img.shields.io/pypi/pyversions/gwapandas.svg)](https://pypi.org/project/gwapandas/)\n[![Build Status](https://github.com/Jianhua-Wang/gwapandas/actions/workflows/dev.yml/badge.svg)](https://github.com/Jianhua-Wang/gwapandas/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/Jianhua-Wang/gwapandas/branch/main/graphs/badge.svg)](https://codecov.io/github/Jianhua-Wang/gwapandas)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n\n\n\nPython tools for GWAS summary statistics\n\n\n* Documentation: <https://Jianhua-Wang.github.io/gwapandas>\n* GitHub: <https://github.com/Jianhua-Wang/gwapandas>\n* PyPI: <https://pypi.org/project/gwapandas/>\n* Free software: MIT\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n',
    'author': 'Jianhua Wang',
    'author_email': 'jianhua.mert@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Jianhua-Wang/gwapandas',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
