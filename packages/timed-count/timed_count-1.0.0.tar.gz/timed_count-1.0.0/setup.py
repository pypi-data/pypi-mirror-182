# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timed_count']

package_data = \
{'': ['*']}

install_requires = \
['stoppy>=1.0.4,<2.0.0']

setup_kwargs = {
    'name': 'timed-count',
    'version': '1.0.0',
    'description': '`timed-count` provides a generator function that returns an iterator that delays each iteration by the specified time period. It can be used to execute code at a precise frequency.',
    'long_description': "# timed-count\n\n`timed-count` provides a generator function that returns an iterator that delays each iteration by the specified time period. It can be used to execute code at a precise frequency.\n\n`timed-count` is a good replacement for a loop that contains a call to `time.sleep`. It is precise, does not dependent on the loop execution time, and won't accumulate temporal drift.\n\n## Installation\n\nInstall from [PyPI](https://pypi.org/project/timed-count/) via:\n\n```shell\npip install timed-count\n```\n\n## Usage\n\nBasic usage is as follows:\n\n```python\nfrom timed_count import timed_count\n\nfor count in timed_count(0.5):\n    # Prints at exactly every half a second\n    print(count)\n```\n\n```python\nTimedCount(index=0, count=0.0, time=0.000, lag=0.000)\nTimedCount(index=1, count=0.5, time=0.500, lag=0.000)\nTimedCount(index=2, count=1.0, time=1.000, lag=0.000)\n...\n```\nFor all usage examples see [examples/](https://github.com/morefigs/timed-count/tree/main/examples).\n",
    'author': 'morefigs',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/morefigs/timed-count',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
