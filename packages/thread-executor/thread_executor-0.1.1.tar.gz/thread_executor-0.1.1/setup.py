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
    'version': '0.1.1',
    'description': 'A Python library for executing tasks in parallel with threads and queues',
    'long_description': '# executor\nfast exec task with python and less mem ops\n\n\n## Why we need executor?\n\nPython threading module is a good structure, it\'s help developer folk a thread to run some background task.\nPython have Queue mechanic to connect thread data.\nBut what problem??\n\n- First, threading module folk threads but python not commit late time. Then know your thread can run, but you don\'t know when? It\'s oke fast with small traffic but when server high load you will have some problem, high pressure on memory because when you create too many thread cause slowness. `waste of time`\n\n- Second, when you create and release thread many times, it\'ll increase memory and CPU time of system. Sometime, developers did not handle exceptions and release thread, It can put more pressure to the application. `waste of resource`\n\n## How to resolve problem??\n\nThis\'s my resolver.\n\n- We create `exact` or `dynamic` number of threads. Then using `Job` is a unit bring data information to `Worker` to process. Workers don\'t need to release, and you only create 1 time or reset it when you update config.\n\n- Job bring 2 importance field is: `func` and `args` and you can call them like `func(*args)` and get all the results and return on `callback` is optional.\n- Your app doesn\'t need to create and release threads continuously\n- Easy to access and using when coding.\n\n## Disadvance?\n\n- If you use callback then remembered to add try catch to handle thread leak.\n- If queue is full you need to wait for available queue slot. set `max_queue_size=0` to avoid this.\n\n## Installtion\n\nNow it\'s time you can install lib and experience\n\n```bash\npip install thread-executor\n```\n\n## Usage : Interface list\n```go\ntype ISafeQueue interface {\n\tInfo() SafeQueueInfo // engine info\n\tClose() error // close all anything\n\tRescaleUp(numWorker uint) // increase worker\n\tRescaleDown(numWorker uint) error // reduce worker\n\tRun() // start\n\tSend(jobs ...*Job) error // push job to hub\n\tWait() // keep block thread\n\tDone() // Immediate stop wait\n}\n```\n\n### Initial\n```go\n    engine = CreateSafeQueue(&SafeQueueConfig{\n        NumberWorkers: 3,\n        Capacity: 500,\n        WaitGroup: &sync.WaitGroup{},\n    })\n    defer engine.Close() // flush engine\n\n    // go engine.Wait() // folk to other thread\n    engine.Wait() // block current thread\n```\n### Send Simple Job\n```go\n    // simple job\n    j := &Job{\n        Exectutor: func(in ...interface{}) {\n            // any thing\n        },\n        Params: []interface{1, "abc"}\n    }\n    engine.Send(j)\n    // send mutiple job\n    jobs := []*Job{\n        {\n             Exectutor: func(in ...interface{}) {\n            // any thing\n        },\n        Params: []interface{1, "abc"}\n        },\n         Exectutor: func(in ...interface{}) {\n            // any thing\n        },\n        Params: []interface{2, "abc"}\n    }\n    engine.Send(jobs...)\n```\n\n### Send Job complicated\n```go\n    // wait for job completed\n    j := &Job{\n        Exectutor: func(in ...interface{}) {\n            // any thing\n        },\n        Params: []interface{1, "abc"},\n        Wg: &sync.WaitGroup{},\n    }\n    engine.Send(j)\n    // wait for job run success\n    j.Wait()\n\n    // callback handle async\n    // you can sync when use with waitgroup\n    j := &Job{\n        Exectutor: func(in ...interface{}) {\n            // any thing\n        },\n        CallBack: func(out interface{}, err error) {\n            // try some thing here\n        }\n        Params: []interface{1, "abc"}\n    }\n    engine.Send(j)\n```\n\n\n### Send Job with groups\n```go\n    // prepaire a group job.\n\tgroup1 := make([]*Job, 0)\n\tfor i := 0; i < 10; i++ {\n\t\tgroup1 = append(group1, &Job{\n            Exectutor: func(in ...interface{}) {\n                // any thing\n            },\n            Params: []interface{1, "abc"},\n            Wg: &sync.WaitGroup{},\n        })\n\t}\n    // wait for job completed\n\tengine.SendWithGroup(group1...)\n\n    engine.Wait()\n```\n\n### safequeue scale up/down\n\n```go\n    engine.ScaleUp(5)\n    engine.ScaleDown(2)\n```\n',
    'author': 'TuanDC',
    'author_email': 'tuandao864@gmail.com',
    'maintainer': 'TuanDC',
    'maintainer_email': 'tuandao864@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
