# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lunchable',
 'lunchable._config',
 'lunchable.models',
 'lunchable.plugins',
 'lunchable.plugins.pushlunch',
 'lunchable.plugins.splitlunch']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1', 'pydantic>=1.2.0,<2.0.0', 'requests>=2,<3', 'rich>=10.0.0']

extras_require = \
{'all': ['splitwise>=2.3.0', 'python-dateutil>=2.8.2,<3.0.0'],
 'splitlunch': ['splitwise>=2.3.0', 'python-dateutil>=2.8.2,<3.0.0']}

entry_points = \
{'console_scripts': ['lunchable = lunchable._cli:cli']}

setup_kwargs = {
    'name': 'lunchable',
    'version': '0.3.1',
    'description': 'A simple Python SDK around the Lunch Money Developer API',
    'long_description': '# lunchable\n\n<div align="center">\n<a href="https://github.com/juftin/lunchable">\n  <img src=https://i.imgur.com/FyKDsG3.png\n    width="400" alt="lunchable">\n</a>\n</div>\n\n[![Lunchable Version](https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable)](https://github.com/juftin/lunchable)\n[![PyPI](https://img.shields.io/pypi/pyversions/lunchable)](https://pypi.python.org/pypi/lunchable/)\n[![Docker Image Version](https://img.shields.io/docker/v/juftin/lunchable?color=blue&label=docker&logo=docker)](https://hub.docker.com/r/juftin/lunchable)\n[![Testing Status](https://github.com/juftin/lunchable/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/juftin/lunchable/actions/workflows/tests.yaml?query=branch%3Amain)\n[![GitHub License](https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License)](https://github.com/juftin/lunchable/blob/main/LICENSE)\n\n**lunchable** is a Python Client for the [Lunch Money Developer API](https://lunchmoney.dev). It\'s\nbuilt on top of [pydantic](https://github.com/samuelcolvin/pydantic), it offers an *intuitive* API,\na *simple* CLI, complete coverage of all endpoints, and *plugins* to other external services.\n\n### Installation\n\n```shell\npip install lunchable\n```\n\n### Usage\n\n```python\nfrom typing import Any, Dict, List\n\nfrom lunchable import LunchMoney\nfrom lunchable.models import TransactionObject\n\nlunch = LunchMoney(access_token="xxxxxxxxxxx")\ntransactions: List[TransactionObject] = lunch.get_transactions()\n\nfirst_transaction: TransactionObject = transactions[0]\ntransaction_as_dict: Dict[str, Any] = first_transaction.dict()\n```\n\n```shell\nexport LUNCHMONEY_ACCESS_TOKEN="xxxxxxxxxxx"\nlunchable transactions get --limit 5\nlunchable http -X GET https://dev.lunchmoney.app/v1/assets\n```\n\n### Check out the [**Docs**](https://juftin.com/lunchable/)\n### Looking to contribute? See the [Contributing Guide](docs/source/contributing.md)\n### See the [Changelog](https://github.com/juftin/lunchable/releases)\n\n\n--------------\n--------------\n\n<br/>\n\n[<p align="center" ><img src="https://raw.githubusercontent.com/juftin/juftin/main/static/juftin.png" width="60" height="60"  alt="juftin logo"> </p>](https://github.com/juftin)\n',
    'author': 'Justin Flannery',
    'author_email': 'juftin@juftin.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/juftin/lunchable',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
