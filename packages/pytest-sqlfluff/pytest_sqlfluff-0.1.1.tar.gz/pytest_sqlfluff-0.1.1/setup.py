# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pytest_sqlfluff']
install_requires = \
['pytest>=3.5.0', 'sqlfluff>=1.0.0']

entry_points = \
{'pytest11': ['sqlfluff = pytest_sqlfluff']}

setup_kwargs = {
    'name': 'pytest-sqlfluff',
    'version': '0.1.1',
    'description': 'A pytest plugin to use sqlfluff to enable format checking of sql files.',
    'long_description': '===============\npytest-sqlfluff\n===============\n\n.. image:: https://img.shields.io/pypi/v/pytest-sqlfluff.svg\n    :target: https://pypi.org/project/pytest-sqlfluff\n    :alt: PyPI version\n\n.. image:: https://img.shields.io/pypi/pyversions/pytest-sqlfluff.svg\n    :target: https://pypi.org/project/pytest-sqlfluff\n    :alt: Python versions\n\n.. image:: https://github.com/prsutherland/pytest-sqlfluff/actions/workflows/ci-flow.yml/badge.svg?branch=main\n    :target: https://github.com/prsutherland/pytest-sqlfluff/actions/workflows/ci-flow.yml?branch=main\n    :alt: See Build Status on Github Workflows\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n    :alt: Code Style: Black\n\nA `pytest`_ plugin to use `sqlfluff`_ to enable format checking of sql files.\n\n----\n\n\nFeatures\n--------\n\n* Tests any sql files found in project.\n* Leverages existing `sqlfluff`_ configurations.\n* Skips unchanged sql files.\n\n\nRequirements\n------------\n\n* Python 3.7+\n* `sqlfluff`_ 1.0.0+\n\n\nInstallation\n------------\n\nYou can install `pytest-sqlfluff` via `pip`_ from `PyPI`_::\n\n    $ pip install pytest-sqlfluff\n\n\nUsage\n-----\n\nOut of the box, you can run `pytest-sqlfluff` as argument to `pytest`_::\n\n    $ pytest --sqlfluff\n    ====================================== test session starts ======================================\n    platform darwin -- Python 3.9.6, pytest-7.2.0, pluggy-1.0.0\n    rootdir: /code/github.com/prsutherland/pytest-sqlfluff\n    plugins: sqlfluff-0.1.0\n    collected 1 item\n\n    tests/file.sql .                                                                          [100%]\n\n    ======================================= 1 passed in 0.45s =======================================\n\nTo configure your sqlfluff linting, use the standard `sqlfluff configuration`_ mechanisms. At the very\nleast, you\'ll likely need to set the dialect.::\n\n    [sqlfluff]\n    dialect = postgres\n    ...\n\n\n\n\nContributing\n------------\nContributions are very welcome. Tests can be run with `pytest`_, please ensure\nthe coverage at least stays the same before you submit a pull request.\n\nTo get started::\n\n    $ git clone https://github.com/prsutherland/pytest-sqlfluff.git\n    $ cd pytest-sqlfluff\n    $ poetry install\n\nRun tests::\n\n    $ poetry run pytest\n\nLicense\n-------\n\nDistributed under the terms of the `MIT`_ license, "pytest-sqlfluff" is free and open source software\n\n\nIssues\n------\n\nIf you encounter any problems, please `file an issue`_ along with a detailed description.\n\n.. _`file an issue`: https://github.com/prsutherland/pytest-sqlfluff/issues\n.. _`MIT`: http://opensource.org/licenses/MIT\n.. _`pip`: https://pypi.org/project/pip/\n.. _`PyPI`: https://pypi.org/project\n.. _`pytest`: https://github.com/pytest-dev/pytest\n.. _`sqlfluff`: https://docs.sqlfluff.com/en/stable/\n.. _`sqlfluff configuration`: https://docs.sqlfluff.com/en/stable/configuration.html\n',
    'author': 'Paul Sutherland',
    'author_email': 'paul@homemade-logic.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
