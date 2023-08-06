# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hyx',
 'hyx.bulkhead',
 'hyx.cache',
 'hyx.circuitbreaker',
 'hyx.circularbuffer',
 'hyx.common',
 'hyx.fallback',
 'hyx.ratelimit',
 'hyx.retry',
 'hyx.timeout']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hyx',
    'version': '0.0.2rc0',
    'description': 'Lightweight fault tolerance primitives for your modern Python microservices',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/roma-glushko/hyx/main/img/hyx-logo.png" alt="Hyx">\n</p>\n<p align="center">\n    <em>🧘\u200d♂️️Lightweight fault tolerance primitives for your resilient and modern Python microservices</em>\n</p>\n<p align="center">\n<a href="https://pypi.org/project/hyx" target="_blank">\n    <img src="https://img.shields.io/pypi/v/hyx?color=%2318afba&label=pypi%20package" alt="Package Version">\n</a>\n<a href="https://pypi.org/project/hyx" target="_blank">\n    <img src="https://img.shields.io/pypi/dm/hyx?color=%2318afba" alt="Downloads">\n</a>\n<a href="https://pypi.org/project/hyx" target="_blank">\n  <img src="https://img.shields.io/pypi/pyversions/hyx.svg?color=%2318afba" alt="Supported Python Versions">\n</a>\n</p>\n\n---\n\nHyx provides you with a toolkit that includes common fault tolerance patterns like:\n\n- bulkhead\n- cache\n- circuit breaker\n- circular buffer\n- fallback\n- rate limiter\n- retries\n- timeout / time limiter\n\nAll components are designed to be:\n\n- asyncio-native\n- in-memory first\n- dependency-less\n\nWith that patterns you should be all set to start improving your resiliency right after the library installation.\n\n## Component Map\n\n| Component         | Problem                                                                                                                                                                            | Solution                                                                                                                                                                      | Implemented? |\n|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|\n| 🔁 Retry           | The failures happen sometimes, but they self-recover after a short time                                                                                                            | Automatically retry operation on temporary failures                                                                                                                           | ✅            |\n| 💾 Cache           |                                                                                                                                                                                    |                                                                                                                                                                               |              |\n| ⚡️ Circuit Breaker | When downstream microservices have got overloaded, sending even more load can make the situation only worse.                                                                       | Stop doing requests to your failing microservice temporarily if amount of errors exceeded expected thresholds. Then see if the given time helped the microservice to recover  | ✅            |\n| ⏱ Timeout         | Sometimes operations may take too much time. We cannot wait that long or after that time the success is unlikely                                                                   | Bound waiting to a reasonable amount of time                                                                                                                                  | ✅            |\n| 🚰 Bulkhead        | If executed without control, some code can take too much resources and put down the whole application (and upstream services) or cause slowness of other places of the application | Fix the amount of calls to the code, queue other calls and fail calls that goes beyond your capacity                                                                          | ✅            |\n| 🏃\u200d♂️ Rate Limiter   |                                                                                                                                                                                    |                                                                                                                                                                               |              |\n| 🤝 Fallback        | Nothing can guarantee you that your dependencies will work. What would you do when it\'s failing?                                                                                   | Degrade gracefully by defining some default values or placeholders if your dependencies are down                                                                              | ✅            |\n\n<p align="right">\nInspired by <a href="https://github.com/App-vNext/Polly#resilience-policies" target="_blank">Polly\'s Resiliency Policies</a>\n</p>\n\n## Acknowledgements\n\n- [resilience4j/resilience4j](https://github.com/resilience4j/resilience4j)\n- [Netflix/Hystrix](https://github.com/Netflix/Hystrix)\n- [slok/goresilience](https://github.com/slok/goresilience)\n- [App-vNext/Polly](https://github.com/App-vNext/Polly)\n- [Diplomatiq/resily](https://github.com/Diplomatiq/resily)\n',
    'author': 'Roman Glushko',
    'author_email': 'roman.glushko.m@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
