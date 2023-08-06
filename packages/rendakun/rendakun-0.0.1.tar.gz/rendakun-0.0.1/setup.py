# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rendakun']

package_data = \
{'': ['*']}

install_requires = \
['pyautogui>=0.9.53,<0.10.0',
 'pyqt6>=6.4.0,<7.0.0',
 'types-pyautogui>=0.9.3.2,<0.10.0.0']

extras_require = \
{'build:python_version < "3.12"': ['pyinstaller>=5.7.0,<6.0.0']}

entry_points = \
{'console_scripts': ['rendakun = rendakun:main']}

setup_kwargs = {
    'name': 'rendakun',
    'version': '0.0.1',
    'description': 'A Python Clone of 連打くん - rendakun, auto-clicker for Windows',
    'long_description': '# rendakun.py\n\n![screenshot](https://user-images.githubusercontent.com/42153744/209469016-63c80c2f-c5b5-4c80-ad91-85e25580512f.png)\n\n[![PyPI version](\n  https://badge.fury.io/py/rendakun.svg\n  )](\n  https://badge.fury.io/py/rendakun\n) [![Maintainability](\n  https://api.codeclimate.com/v1/badges/548eef5a0ef654357f8e/maintainability\n  )](\n  https://codeclimate.com/github/eggplants/rendakun.py/maintainability\n) [![pre-commit.ci status](\n  https://results.pre-commit.ci/badge/github/eggplants/rendakun.py/master.svg\n  )](\n  https://results.pre-commit.ci/latest/github/eggplants/rendakun.py/master\n)\n\nA Clone of [連打くん - rendakun, auto-clicker for Windows](https://www.vector.co.jp/soft/win95/util/se420838.html) in Python\n\n```bash\npip install git+https://github.com/eggplants/rendakun.py\n\nrendakun # launch\n```\n',
    'author': 'eggplants',
    'author_email': 'w10776e8w@yahoo.co.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eggplants/rendakun.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
