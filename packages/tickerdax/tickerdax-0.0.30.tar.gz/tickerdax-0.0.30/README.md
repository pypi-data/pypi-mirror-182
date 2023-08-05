<p align="center">
  <img width="200" src="https://tickerdax.com/assets/images/logo/logo.svg" alt="icon"/>
</p>
<h1 align="center">TickerDax Client</h1>
<br></br>

[![CI](https://github.com/TickerDax/tickerdax-client/actions/workflows/ci.yaml/badge.svg)](https://github.com/TickerDax/tickerdax-client/actions/workflows/ci.yaml)

A python package that interfaces with the tickerdax.com REST and websockets API. It handles common data operations
like batch downloading data, streaming real-time data, and caching data locally to minimize network requests.

## Installation
You can install this package with pip by running the command below.
```shell
pip install tickerdax
```

## Docker Dependency
This client interfaces with a redis docker container. In order for the package to work, you must first install
docker. Here are instructions per platform.
### Mac
[Instructions](https://docs.docker.com/desktop/install/mac-install/)
### Linux
[Instructions](https://docs.docker.com/desktop/install/linux-install/)
### Windows
Note on windows you must first install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) then you can install docker.
[Instructions](https://docs.docker.com/desktop/install/windows-install/)

## Python Examples
Here is a basic example of getting historical data using the python SDK.
### Get historical data
```python
from pprint import pprint
from datetime import datetime, timezone
from tickerdax.client import TickerDax

client = TickerDax()
pprint(client.get_route(
    route='predictions/ml-order-book-model-1',
    symbols=["BTC"],
    start=datetime.now(tz=timezone.utc),
    end=datetime.now(tz=timezone.utc)
))
```
Note that if this data doesn't exist in your cache, the data will be fetched from the REST API. All
subsequent calls to the same data will only be from the cache and not the REST API.
This is designed give you lighting fast responses and ultimately deliver data to you a cheaper cost.

### Stream realtime data
This is how you can stream data to your cache. This will run indefinitely and fill
your local cache as new data is available.
```python
client.stream(
    routes={
        'predictions/ml-order-book-model-1': ['BTC', 'LTC'],
    },
)
```
In another process you can call `client.get_route()` as many times you like or whenever your
app re-evaluates. The data will be available once it is updated by the stream.


## CLI

The TickerDax CLI tool interfaces with the tickerdax.com REST and websockets APIs. It
handles common data operations like batch downloading, streaming, and caching data
locally to minimize network requests.

**Usage**:

```console
$ tickerdax [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--version`
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `create-config`: Creates a new ticker dax config.
* `download`: Downloads data from the routes with the...
* `list-routes`: Lists all routes available to download or...
* `stream`: Streams data from the routes specified in...

## `tickerdax create-config`

Creates a new ticker dax config.

**Usage**:

```console
$ tickerdax create-config [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `tickerdax download`

Downloads data from the routes with the time interval specified in your config.

**Usage**:

```console
$ tickerdax download [OPTIONS] [CONFIG] [REST_API_KEY]
```

**Arguments**:

* `[CONFIG]`: A file path to the config file for the CLI.  [env var: TICKERDAX_CONFIG]
* `[REST_API_KEY]`: Your REST API created with your tickerdax.com account.  [env var: TICKERDAX_REST_API_KEY]

**Options**:

* `--force / --no-force`: Forces new REST requests for all missing data, even if that data has already been marked as missing  [default: no-force]
* `--help`: Show this message and exit.

## `tickerdax list-routes`

Lists all routes available to download or stream.

**Usage**:

```console
$ tickerdax list-routes [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `tickerdax stream`

Streams data from the routes specified in your config.

**Usage**:

```console
$ tickerdax stream [OPTIONS] [CONFIG] [REST_API_KEY] [WEBSOCKET_API_KEY]
```

**Arguments**:

* `[CONFIG]`: A file path to the config file for the CLI.  [env var: TICKERDAX_CONFIG]
* `[REST_API_KEY]`: Your REST API created with your tickerdax.com account.  [env var: TICKERDAX_REST_API_KEY]
* `[WEBSOCKET_API_KEY]`: Your websocket API created with your tickerdax.com account.   [env var: TICKERDAX_WEBSOCKET_API_KEY]

**Options**:

* `--force / --no-force`: Forces new REST requests for all missing data, even if that data has already been marked as missing  [default: no-force]
* `--help`: Show this message and exit.


## Environment Variables
| Name                             | Description                                                                                                                                |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `TICKERDAX_CONFIG` | A file path to the config file for the CLI. |
| `TICKERDAX_EMAIL` | Your email linked to your tickerdax.com account. |
| `TICKERDAX_REST_API_KEY` | Your REST API created with your tickerdax.com account. |
| `TICKERDAX_WEBSOCKET_API_KEY` | Your websocket API created with your tickerdax.com account.  |
| `TICKERDAX_CACHE_ROOT` | An alternative persistent cache location on disk. By default this is written into a `tickerdax_cache` folder in your system's temp folder. |
| `TICKERDAX_REDIS_SERVER_ADDRESS` | An alternative redis server address. Can be useful if redis is on another address besides localhost. |
| `TICKERDAX_REDIS_SERVER_PORT` | An alternative redis server port. Can be useful if redis needs to user another port besides `6379`. |
