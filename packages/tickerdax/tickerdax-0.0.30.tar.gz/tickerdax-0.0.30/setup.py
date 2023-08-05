# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tickerdax']

package_data = \
{'': ['*'], 'tickerdax': ['example_configs/*']}

install_requires = \
['art>=5.8,<6.0',
 'docker>=6.0.1,<7.0.0',
 'fastapi>=0.88.0,<0.89.0',
 'jinja2>=3.1.2,<4.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'pyyaml>=6.0,<7.0',
 'redis>=4.4.0,<5.0.0',
 'schema>=0.7.5,<0.8.0',
 'tomlkit>=0.11.6,<0.12.0',
 'typer[all]>=0.7.0,<0.8.0',
 'uvicorn>=0.20.0,<0.21.0',
 'websockets>=10.4,<11.0']

entry_points = \
{'console_scripts': ['tickerdax = tickerdax.cli:app']}

setup_kwargs = {
    'name': 'tickerdax',
    'version': '0.0.30',
    'description': 'A python client for tickerdax.com with a built-in caching system.',
    'long_description': '<p align="center">\n  <img width="200" src="https://tickerdax.com/assets/images/logo/logo.svg" alt="icon"/>\n</p>\n<h1 align="center">TickerDax Client</h1>\n<br></br>\n\n[![CI](https://github.com/TickerDax/tickerdax-client/actions/workflows/ci.yaml/badge.svg)](https://github.com/TickerDax/tickerdax-client/actions/workflows/ci.yaml)\n\nA python package that interfaces with the tickerdax.com REST and websockets API. It handles common data operations\nlike batch downloading data, streaming real-time data, and caching data locally to minimize network requests.\n\n## Installation\nYou can install this package with pip by running the command below.\n```shell\npip install tickerdax\n```\n\n## Docker Dependency\nThis client interfaces with a redis docker container. In order for the package to work, you must first install\ndocker. Here are instructions per platform.\n### Mac\n[Instructions](https://docs.docker.com/desktop/install/mac-install/)\n### Linux\n[Instructions](https://docs.docker.com/desktop/install/linux-install/)\n### Windows\nNote on windows you must first install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) then you can install docker.\n[Instructions](https://docs.docker.com/desktop/install/windows-install/)\n\n## Python Examples\nHere is a basic example of getting historical data using the python SDK.\n### Get historical data\n```python\nfrom pprint import pprint\nfrom datetime import datetime, timezone\nfrom tickerdax.client import TickerDax\n\nclient = TickerDax()\npprint(client.get_route(\n    route=\'predictions/ml-order-book-model-1\',\n    symbols=["BTC"],\n    start=datetime.now(tz=timezone.utc),\n    end=datetime.now(tz=timezone.utc)\n))\n```\nNote that if this data doesn\'t exist in your cache, the data will be fetched from the REST API. All\nsubsequent calls to the same data will only be from the cache and not the REST API.\nThis is designed give you lighting fast responses and ultimately deliver data to you a cheaper cost.\n\n### Stream realtime data\nThis is how you can stream data to your cache. This will run indefinitely and fill\nyour local cache as new data is available.\n```python\nclient.stream(\n    routes={\n        \'predictions/ml-order-book-model-1\': [\'BTC\', \'LTC\'],\n    },\n)\n```\nIn another process you can call `client.get_route()` as many times you like or whenever your\napp re-evaluates. The data will be available once it is updated by the stream.\n\n\n## CLI\n\nThe TickerDax CLI tool interfaces with the tickerdax.com REST and websockets APIs. It\nhandles common data operations like batch downloading, streaming, and caching data\nlocally to minimize network requests.\n\n**Usage**:\n\n```console\n$ tickerdax [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--version`\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `create-config`: Creates a new ticker dax config.\n* `download`: Downloads data from the routes with the...\n* `list-routes`: Lists all routes available to download or...\n* `stream`: Streams data from the routes specified in...\n\n## `tickerdax create-config`\n\nCreates a new ticker dax config.\n\n**Usage**:\n\n```console\n$ tickerdax create-config [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n## `tickerdax download`\n\nDownloads data from the routes with the time interval specified in your config.\n\n**Usage**:\n\n```console\n$ tickerdax download [OPTIONS] [CONFIG] [REST_API_KEY]\n```\n\n**Arguments**:\n\n* `[CONFIG]`: A file path to the config file for the CLI.  [env var: TICKERDAX_CONFIG]\n* `[REST_API_KEY]`: Your REST API created with your tickerdax.com account.  [env var: TICKERDAX_REST_API_KEY]\n\n**Options**:\n\n* `--force / --no-force`: Forces new REST requests for all missing data, even if that data has already been marked as missing  [default: no-force]\n* `--help`: Show this message and exit.\n\n## `tickerdax list-routes`\n\nLists all routes available to download or stream.\n\n**Usage**:\n\n```console\n$ tickerdax list-routes [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n## `tickerdax stream`\n\nStreams data from the routes specified in your config.\n\n**Usage**:\n\n```console\n$ tickerdax stream [OPTIONS] [CONFIG] [REST_API_KEY] [WEBSOCKET_API_KEY]\n```\n\n**Arguments**:\n\n* `[CONFIG]`: A file path to the config file for the CLI.  [env var: TICKERDAX_CONFIG]\n* `[REST_API_KEY]`: Your REST API created with your tickerdax.com account.  [env var: TICKERDAX_REST_API_KEY]\n* `[WEBSOCKET_API_KEY]`: Your websocket API created with your tickerdax.com account.   [env var: TICKERDAX_WEBSOCKET_API_KEY]\n\n**Options**:\n\n* `--force / --no-force`: Forces new REST requests for all missing data, even if that data has already been marked as missing  [default: no-force]\n* `--help`: Show this message and exit.\n\n\n## Environment Variables\n| Name                             | Description                                                                                                                                |\n|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|\n| `TICKERDAX_CONFIG` | A file path to the config file for the CLI. |\n| `TICKERDAX_EMAIL` | Your email linked to your tickerdax.com account. |\n| `TICKERDAX_REST_API_KEY` | Your REST API created with your tickerdax.com account. |\n| `TICKERDAX_WEBSOCKET_API_KEY` | Your websocket API created with your tickerdax.com account.  |\n| `TICKERDAX_CACHE_ROOT` | An alternative persistent cache location on disk. By default this is written into a `tickerdax_cache` folder in your system\'s temp folder. |\n| `TICKERDAX_REDIS_SERVER_ADDRESS` | An alternative redis server address. Can be useful if redis is on another address besides localhost. |\n| `TICKERDAX_REDIS_SERVER_PORT` | An alternative redis server port. Can be useful if redis needs to user another port besides `6379`. |\n',
    'author': 'tickerdax.com',
    'author_email': 'info@tickerdax.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tickerdax/tickerdax-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0.0',
}


setup(**setup_kwargs)
