# trio-asgi-server

An [ASGI][asgi] server for [trio][trio].

It can be used directly, or as a [gunicorn][gunicorn] worker.


## Quickstart

Install using `pip`:

```shell
$ pip install trio-asgi-server
```

Create an application, in `app.py`:

```python
class App():
    def __init__(self, scope):
        self.scope = scope

    async def __call__(self, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': b'Hello, world!',
        })
```


### 1. Standalone mode

Run the server:

```shell
$ trio-asgi app:App
```


### 2. Gunicorn worker

```shell
gunicorn --worker-class trio_asgi.workers.H11Worker app:App
```


## Stack

This module depends on [uvicorn][uvicorn] and [trio-protocol][trio-protocol].

[uvicorn][uvicorn] is the main workhorse and provides the two actual ASGI implementations (one
based on [h11][h11], one based on [httptools][httptools]) as an asyncio `Protocol`.

[trio-protocol][trio-protocol] provides lightweight glue to let trio run those protocols.


[trio]: https://github.com/python-trio/trio
[asgi]: https://github.com/django/asgiref/blob/master/specs/asgi.rst
[gunicorn]: [http://gunicorn.org/]
[httptools]: https://github.com/MagicStack/httptools
[h11]: https://github.com/python-hyper/h11
[uvicorn]: https://github.com/encode/uvicorn
[trio-protocol]: https://github.com/miracle2k/trio-protocol