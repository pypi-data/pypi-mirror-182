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
The package also has a command line interface.
```text
 _____  ___   ____  _  __ _____  ____   ____      _    __  __
|_   _||_ _| / ___|| |/ /| ____||  _ \ |  _ \    / \   \ \/ /
  | |   | | | |    | ' / |  _|  | |_) || | | |  / _ \   \  / 
  | |   | | | |___ | . \ | |___ |  _ < | |_| | / ___ \  /  \ 
  |_|  |___| \____||_|\_\|_____||_| \_\|____/ /_/   \_\/_/\_\
                                                             

[1m                                                                                [0m
[1m [0m[1;33mUsage: [0m[1mcallback [OPTIONS] COMMAND [ARGS]...[0m[1m                                   [0m[1m [0m
[1m                                                                                [0m
 TickerDax CLI 0.0.29. This tool interfaces with the tickerdax.com REST and     
 websockets APIs. Ithandles common data operations like batch downloading,      
 streaming, and caching datalocally to minimize network requests.               
                                                                                
[2m╭─[0m[2m Options [0m[2m───────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36m-[0m[1;36m-version[0m                                                                    [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-install[0m[1;36m-completion[0m          Install completion for the current shell.      [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-show[0m[1;36m-completion[0m             Show completion for the current shell, to copy [2m│[0m
[2m│[0m                               it or customize the installation.              [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-help[0m                        Show this message and exit.                    [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m
[2m╭─[0m[2m Commands [0m[2m──────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36mcreate-config[0m[1;36m [0m Creates a new ticker dax config.                              [2m│[0m
[2m│[0m [1;36mdownload     [0m[1;36m [0m Downloads data from the routes with the time interval         [2m│[0m
[2m│[0m [1;36m              [0m specified in your config.                                     [2m│[0m
[2m│[0m [1;36mlist-routes  [0m[1;36m [0m Lists all routes available to download or stream.             [2m│[0m
[2m│[0m [1;36mstream       [0m[1;36m [0m Streams data from the routes specified in your config.        [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m


```

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
