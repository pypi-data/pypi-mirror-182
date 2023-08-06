# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pie_lock',
 'pie_lock.backends',
 'pie_lock.backends.distributed_lock',
 'pie_lock.backends.optimistic_lock',
 'pie_lock.tests']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.2,<2.0.0',
 'async-timeout>=4.0.2,<5.0.0',
 'inflection>=0.5.1,<0.6.0',
 'redis>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'pie-lock',
    'version': '0.1.6',
    'description': 'A library for python distributed lock and optimistic lock',
    'long_description': '# Pie-lock\nAll lock module  using redis for control.\n## Installation\nWith Pypi:\n``` bash\npip install pie-lock\n```\n\nWith Github:\n``` bash\npip install git+https://github.com/HKer-MuCoi/pielock.git\n```\n\n## Usage Distributed Lock\n``` python3\nkey = "test1"\nsuccess, msg = redis_lock.acquire(key)\nprint(msg)\nif not success:\n    print(msg)\nredis_lock.release(key)\n```\n\n## Usage Optimistic Lock\n``` python3\ndef test_optimistic_lock(self):\n    is_locked1, msg = redis_lock.acquire("key1")\n    if not is_locked1:\n        print(msg)\n    is_locked2, msg = redis_lock.acquire("key1")\n    if not is_locked2:\n        print(msg)\n    is_locked3, msg = redis_lock.acquire("key1")\n    if not is_locked3:\n        print(msg)\n    release, msg = redis_lock.release("key1")\n    if not release:\n        print(msg)\n    is_locked4, msg = redis_lock.acquire("key1")\n    if not is_locked4:\n        print(msg)\n```\n## Configuration\n\nRedis configuration\n``` python3\nfrom pie_lock.backends import OptimisticLock\n\nredis_lock = DistributedLock(\n    expires=5,\n    timeout=5,\n    retry_after=1, # seconds between retries\n    tries=32,  # max number of tries\n)\nredis_lock.get_client(\n    host="localhost",\n    port=19821,\n    password="passsword",\n    username="default"\n)\n```\n\nNote: all fields after the scheme are optional, and will default to\nlocalhost on port 6379, using database 0.\n\n\n``DEFAULT_TIMEOUT`` (default: 60)\n\nIf another client has already obtained the lock, sleep for a maximum of\nthis many seconds before giving up. A value of 0 means no wait (give up\nright away).\n\nThe default timeout can be overridden when instantiating the lock.\n\n``DEFAULT_EXPIRES`` (default: 10)\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nWe consider any existing lock older than this many seconds to be invalid\nin order to detect crashed clients. This value must be higher than it\ntakes the critical section to execute.\n\nThe default expires can be overridden when instantiating the lock.\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',
    'author': 'TuanDC',
    'author_email': 'tuandao864@gmail.com',
    'maintainer': 'TuanDC',
    'maintainer_email': 'tuandao864@gmail.com',
    'url': 'https://pypi.org/project/pie-lock',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
