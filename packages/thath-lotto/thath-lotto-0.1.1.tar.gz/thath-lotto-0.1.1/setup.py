# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lotto']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['lotto = lotto.cli:cli']}

setup_kwargs = {
    'name': 'thath-lotto',
    'version': '0.1.1',
    'description': 'This is a small lottery game',
    'long_description': None,
    'author': 'Travis Hathaway',
    'author_email': 'travis.j.hathaway@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
