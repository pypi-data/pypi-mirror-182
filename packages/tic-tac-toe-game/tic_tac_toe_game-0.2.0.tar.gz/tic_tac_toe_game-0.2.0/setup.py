# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tic_tac_toe_game', 'tic_tac_toe_game.AI']

package_data = \
{'': ['*']}

install_requires = \
['Flask-Assets>=2.0,<3.0',
 'Flask-Migrate>=4.0.0,<5.0.0',
 'Flask-SQLAlchemy>=3.0.2,<4.0.0',
 'Flask-Session>=0.4.0,<0.5.0',
 'Flask-SocketIO>=5.3.2,<6.0.0',
 'Flask-WTF>=1.0.1,<2.0.0',
 'Flask>=2.2.2,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'easyAI>=2.0.12,<3.0.0',
 'eventlet>=0.33.2,<0.34.0',
 'gunicorn>=20.1.0,<21.0.0',
 'mctspy>=0.1.1,<0.2.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'redis>=4.4.0,<5.0.0',
 'rich>=12.6.0,<13.0.0',
 'structlog>=22.3.0,<23.0.0']

entry_points = \
{'console_scripts': ['game = app.__main__:main',
                     'tic-tac-toe-game = tic_tac_toe_game.__main__:main']}

setup_kwargs = {
    'name': 'tic-tac-toe-game',
    'version': '0.2.0',
    'description': 'Tic Tac Toe Game',
    'long_description': "# Tic Tac Toe Game\n\n[![PyPI](https://img.shields.io/pypi/v/tic-tac-toe-game.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/tic-tac-toe-game.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/tic-tac-toe-game)][pypi status]\n[![License](https://img.shields.io/pypi/l/tic-tac-toe-game)][license]\n\n[![Read the documentation at https://tic-tac-toe-game.readthedocs.io/](https://img.shields.io/readthedocs/tic-tac-toe-game/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/alexistli/tic-tac-toe-game/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/alexistli/tic-tac-toe-game/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi status]: https://pypi.org/project/tic-tac-toe-game/\n[read the docs]: https://tic-tac-toe-game.readthedocs.io/\n[tests]: https://github.com/alexistli/tic-tac-toe-game/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/alexistli/tic-tac-toe-game\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Tic Tac Toe Game_ via [pip] from [PyPI]:\n\n```console\n$ pip install tic-tac-toe-game\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Tic Tac Toe Game_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/alexistli/tic-tac-toe-game/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/alexistli/tic-tac-toe-game/blob/main/LICENSE\n[contributor guide]: https://github.com/alexistli/tic-tac-toe-game/blob/main/CONTRIBUTING.md\n[command-line reference]: https://tic-tac-toe-game.readthedocs.io/en/latest/usage.html\n",
    'author': 'Alexis Torelli',
    'author_email': 'alexis.torelli.treanton@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alexistli/tic-tac-toe-game',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
