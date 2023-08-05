# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logstamp']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'logstamp',
    'version': '0.1.0',
    'description': 'Logstamp console and file log.',
    'long_description': '# logstamp\n\nAnother logger, made for data science and heavy-compute workloads. Logs to timestamped file too.\n\n## Usage\n\n```python3\nfrom logstamp import log\nimport time\nlog("doing big thing")\ntime.sleep(3)\nlog("did big thing, doing other thing")\ntime.sleep(5)\nlog("all done")\n```\n\n## logs to file:\n\n```Started script ... is now 2022-12-19 18:05:22.769841 ... last interval 0:00:00.000001\ndoing big thing ... is now 2022-12-19 18:05:22.769930 ... last interval 0:00:00.000089\ndid big thing, doing other thing ... is now 2022-12-19 18:05:25.773236 ... last interval 0:00:03.003306\nall done ... is now 2022-12-19 18:05:30.778863 ... last interval 0:00:05.005627\n```',
    'author': 'Andrew MAtte',
    'author_email': 'andrew.matte@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
