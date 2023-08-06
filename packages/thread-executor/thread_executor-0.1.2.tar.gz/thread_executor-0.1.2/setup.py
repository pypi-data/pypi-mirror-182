# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['executor']

package_data = \
{'': ['*']}

modules = \
['safe_queue']
install_requires = \
['loguru>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'thread-executor',
    'version': '0.1.2',
    'description': 'A Python library for executing tasks in parallel with threads and queues',
    'long_description': '# Executor\nFast execute task with python and less mem ops\n\n\n## Why we need Thread Executor?\n\nPython threading module is a good structure, it helps developers to folk a thread to run some background tasks.\nPython have Queue mechanism to connect thread data.\nBut what problem??\n\n- First, threading module folk threads but python not commit late time. Then know your thread can run, but you don\'t know when? It\'s oke fast with small traffic but when server high load you will have some problem, high pressure on memory because when you create too many thread cause slowness. `waste of time`\n\n- Second, when you create and release threads many times, it\'ll increase memory and CPUs time of system. Sometime, developers did not handle exceptions and release thread. It can put more pressure to the application. `waste of resource`\n\n## How to resolve problem??\n\nThis\'s my resolver.\n\n- We create `exact` or `dynamic` number of threads. Then using `Job` - a unit bring data information to `Worker` to process. Workers don\'t need to release, and you only create 1 time or reset it when you update config.\n\n- Job bring 2 importance field is: `func` and `args` and you can call them like `func(*args)` and get all the results and return on `callback` is optional.\n- Your app doesn\'t need to create and release threads continuously\n- Easy to access and using when coding.\n\n## Disadvance?\n\n- If you use callback then remembered to `add try catch` to handle thread leaked.\n- If queue is full you need to wait for available queue slot. set `max_queue_size=0` to avoid this.\n- If you restart your app, all the `Jobs` in `Queue` that have not been processed will be `lost`.\n\n## Installtion\n\nNow it\'s time you can install lib and experience\n\n```bash\npip install thread-executor\n```\n\n## Usage : Interface list\n```python3\nsend(job: Job) -> None # Push a job to the queue\nwait() -> None # wait for all jobs to be completed without blocking each other\nscale_up(number_threads: int) -> None # scale up number of threads\nscale_down(self, number_threads: int) -> None # scale down number of threads\n```\n\n### Initial\n```python3\nfrom executor.safe_queue import Executor, Job\n\nengine = Executor(number_threads=10, max_queue_size=0)\n```\n### Send Simple Job\n```python\nimport time\n\ndef test_exec(*args, **kwargs):\n    time.sleep(3)\n    print(args)\n    return [1, 2, 3]\n\n\ndef test_exec1(*args, **kwargs):\n    print(kwargs)\n    time.sleep(2)\n    return {"a": 1, "b": 2, "c": 3}\n\nengine.send(Job(func=test_exec, args=(1, 2), kwargs={}, callback=None, block=False))\nengine.send(Job(func=test_exec1, args=(), kwargs={"time": 1}, callback=None, block=False))\nengine.send(Job(func=test_exec1, args=(), kwargs={}, callback=None, block=False))\nengine.send(Job(func=test_exec1, args=(), kwargs={}, callback=None, block=False))\nengine.send(Job(func=test_exec1, args=(), kwargs={}, callback=None, block=False))\nengine.wait()\n```\n\n### Send Job with callback\n```python3\ndef call_back(result):\n    print(result)\n    \nfor i in range(5):\n    engine.send(Job(func=test_exec1, args=(), kwargs={"time": 1}, callback=call_back, block=False))\nengine.wait()\n```\n\n\n### Thread scale up/down\n\n```python3\nengine.scale_up(3)\nengine.scale_down(3)\n```\n',
    'author': 'TuanDC',
    'author_email': 'tuandao864@gmail.com',
    'maintainer': 'TuanDC',
    'maintainer_email': 'tuandao864@gmail.com',
    'url': 'https://pypi.org/project/thread-executor',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
