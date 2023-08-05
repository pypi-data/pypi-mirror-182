# Arrlio [WIP]

[Documentation](https://levsh.github.io/arrlio)

Simplest asyncio distributed task/workflow system

![tests](https://github.com/levsh/arrlio/workflows/tests/badge.svg)
![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/levsh/727ed723ccaee0d5825513af6472e3a5/raw/coverage.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

```bash
pip install arrlio
```

```python
import asyncio
import os

import arrlio


@arrlio.task(name="sync hello_world")
def sync_hello_world():
    return "Hello World!"

@arrlio.task(name="async hello_world")
async def async_hello_world():
    return "Hello World!"

BACKEND = "arrlio.backends.local"
# BACKEND = "arrlio.backends.rabbitmq"
# BACKEND = "arrlio.backends.redis"

async def main():
    app = arrlio.App(arrlio.Config(backend=BACKEND))
    # app = arrlio.App(arrlio.Config(backend=lambda: backends.local.Backend(backends.local.BackendConfig())))

    async with app:
        await app.consume_tasks()

        ar = await app.send_task("sync hello_world")
        print(await ar.get())

        ar = await app.send_task("async hello_world")
        print(await ar.get())


asyncio.run(main())
```

```python
import asyncio
import os

import arrlio


@arrlio.task
async def add_one(value: str):
    return int(value) + 1

graph = arrlio.Graph("My Graph")
graph.add_node("A", add_one, root=True)
graph.add_node("B", add_one)
graph.add_node("C", add_one)
graph.add_edge("A", "B")
graph.add_edge("B", "C")

BACKEND = "arrlio.backends.local"

async def main():
    app = arrlio.App(arrlio.Config(backend=BACKEND))

    async with app:
        await app.consume_tasks()

        ars = await app.send_graph(graph, args=(0,))
        print(await ars["C"].get())


asyncio.run(main())
```

```python
import asyncio
import os

import arrlio
import invoke


@arrlio.task(thread=True)
async def bash(cmd):
    return invoke.run(cmd).stdout

graph = arrlio.Graph("My Graph")
graph.add_node("A", bash, root=True)
graph.add_node("B", bash, args=("wc -w",))
graph.add_edge("A", "B")

BACKEND = "arrlio.backends.local"

async def main():
    app = arrlio.App(arrlio.Config(backend=BACKEND))

    async with app:
        await app.consume_tasks()

        ars = await app.send_graph(
            graph,
            args=('echo "Number of words in this sentence:"',)
        )
        print(await asyncio.wait_for(ars["B"].get(), timeout=2))


asyncio.run(main())
```

```bash
pipenv install
pipenv run python examples/main.py
```
