# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pjt', 'pjt.cli', 'pjt.core']

package_data = \
{'': ['*']}

install_requires = \
['awesome-pattern-matching>=0.24.3,<0.25.0',
 'cleo>=2.0.1,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'returns>=0.19.0,<0.20.0']

entry_points = \
{'console_scripts': ['pjt = pjt.app:run']}

setup_kwargs = {
    'name': 'pip-jump-to',
    'version': '0.1.0',
    'description': 'pjt (pip-jump-to) - a quick navigation tool for the PyPI packages.',
    'long_description': '<div align="center">\n    <a href="https://pypi.org/project/pip-jump-to">\n        <img alt="logo" src="https://github.com/volopivoshenko/pip-jump-to/blob/main/docs/static/assets/logo.svg?raw=True" height=200>\n    </a>\n</div>\n',
    'author': 'Volodymyr Pivoshenko',
    'author_email': 'volodymyr.pivoshenko@gmail.com',
    'maintainer': 'Volodymyr Pivoshenko',
    'maintainer_email': 'volodymyr.pivoshenko@gmail.com',
    'url': 'https://github.com/volopivoshenko/pip-jump-to',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
