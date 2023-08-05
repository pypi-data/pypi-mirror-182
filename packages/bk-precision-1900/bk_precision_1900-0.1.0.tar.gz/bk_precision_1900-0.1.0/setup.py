# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bk_precision_1900']

package_data = \
{'': ['*']}

install_requires = \
['pyserial>=3.5,<4.0']

entry_points = \
{'console_scripts': ['bk_ctrl = bk.bk_demo:cli']}

setup_kwargs = {
    'name': 'bk-precision-1900',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Carlos Asmat',
    'author_email': 'casmat@dephy.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
