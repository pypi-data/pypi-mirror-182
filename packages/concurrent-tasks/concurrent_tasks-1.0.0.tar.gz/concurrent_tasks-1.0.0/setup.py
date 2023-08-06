# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['concurrent_tasks', 'concurrent_tasks.threaded_pool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'concurrent-tasks',
    'version': '1.0.0',
    'description': 'Tools to run asyncio tasks concurrently.',
    'long_description': "# asyncio-concurrent-tasks\n\n[![tests](https://github.com/gpajot/asyncio-concurrent-tasks/workflows/Test/badge.svg?branch=main&event=push)](https://github.com/gpajot/asyncio-concurrent-tasks/actions?query=workflow%3ATest+branch%3Amain+event%3Apush)\n[![version](https://img.shields.io/pypi/v/concurrent_tasks?label=stable)](https://pypi.org/project/concurrent_tasks/)\n[![python](https://img.shields.io/pypi/pyversions/concurrent_tasks)](https://pypi.org/project/concurrent_tasks/)\n\nTooling to run asyncio tasks.\n\n## Background task\nTask that is running in the background until cancelled.\nCan be used as a context manager.\n\nExample usage:\n\n```python\nimport asyncio\nfrom typing import Callable, Awaitable\nfrom concurrent_tasks import BackgroundTask\n\n\nclass HeartBeat(BackgroundTask):\n    def __init__(self, interval: float, func: Callable[[], None]):\n        super().__init__(self._run, interval, func)\n\n    async def _run(self, interval: float, func: Callable[[], Awaitable]) -> None:\n        while True:\n            await func()\n            await asyncio.sleep(interval)\n```\n\n## Threaded task pool\nRun async tasks in a dedicated thread. It will have its own event loop.\n\nParameters:\n- `name` will be used as the thread's name.\n- `size` can be a positive integer to limit the number of tasks concurrently running.\n- `timeout` can be set to define a maximum running time for each time after which it will be cancelled.\nNote: this excludes time spent waiting to be started (time spent in the buffer).\n- `context_manager` can be optional context managers that will be entered when the loop has started\nand exited before the loop is stopped.\n\n> 💡 All tasks will be completed when the pool is stopped.\n\n> 💡Blocking and async version are the same, prefer the async version if client code is async.\n\n### Blocking\nThis can be used to run async functions in a dedicated event loop, while keeping it running to handle background tasks\n\nExample usage:\n\n```python\nfrom concurrent_tasks import BlockingThreadedTaskPool\n\n\nasync def func():\n    ...\n\n\nwith BlockingThreadedTaskPool() as pool:\n    # Create and run the task.\n    result = pool.run(func())\n    # Create a task, the future will hold information about completion.\n    future = pool.create_task(func())\n```\n\n### Async\nThreads can be useful in cooperation with asyncio to let the OS guarantee fair resource distribution between threads.\nThis is especially useful in case you cannot know if called code will properly cooperate with the event loop.\n\nExample usage:\n\n```python\nfrom concurrent_tasks import AsyncThreadedTaskPool\n\n\nasync def func():\n    ...\n\n\nasync with AsyncThreadedTaskPool() as pool:\n    # Create and run the task.\n    result = await pool.run(func())\n    # Create a task, the future will hold information about completion.\n    future = pool.create_task(func())\n```\n",
    'author': 'Gabriel Pajot',
    'author_email': 'gab@les-cactus.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gpajot/asyncio-concurrent-tasks',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
