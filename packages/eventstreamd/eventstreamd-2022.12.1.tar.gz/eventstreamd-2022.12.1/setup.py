# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['evtstrd', 'evtstrd.plugins', 'evtstrd_test']

package_data = \
{'': ['*']}

install_requires = \
['json-get>=1.1.1,<1.2.0']

entry_points = \
{'console_scripts': ['eventstreamd = evtstrd.main:main']}

setup_kwargs = {
    'name': 'eventstreamd',
    'version': '2022.12.1',
    'description': 'Simple Event Stream Server',
    'long_description': '# eventstreamd\n\n[![License](https://img.shields.io/pypi/l/eventstreamd.svg)](https://pypi.python.org/pypi/eventstreamd/)\n[![GitHub](https://img.shields.io/github/release/srittau/eventstreamd/all.svg)](https://github.com/srittau/eventstreamd/releases/)\n[![pypi](https://img.shields.io/pypi/v/eventstreamd.svg)](https://pypi.python.org/pypi/eventstreamd/)\n[![Travis CI](https://travis-ci.org/srittau/eventstreamd.svg?branch=master)](https://travis-ci.org/srittau/eventstreamd)\n\nA simple event stream server. Events are sent on a Unix socket and then\ndistributed to all interested listeners via HTTP event streams.\n\nDocker image available:\n\n```bash\ndocker pull srittau/eventstreamd\n```\n',
    'author': 'Sebastian Rittau',
    'author_email': 'srittau@rittau.biz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/srittau/eventstreamd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
