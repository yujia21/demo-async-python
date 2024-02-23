# Introduction
Repository with demo code for using async in python.

Three sets of examples follow.

## Sleep
* Demonstrates sleeping synchronously and asynchronously with different libraries.
* Scripts can be run as is: `python sleep_anyio.py`

## HTTP Requester
* Demonstrates requesting data from Singapore government's open data platform with different libraries.
* Scripts can be run as is: `python http_requester_aiohttp.py`.

## Client Server
* Demonstrates two ways of setting up an async server and client, where the server responds the same message to the client after a short pause.
* To run, first start a server script in a terminal with `python echo_server_anyio.py`. Then, in a second terminal, running `python echo_client_anyio.py hello` will send 'hello' to the server.