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
    'version': '0.2.0',
    'description': 'Control the BK Precision 1900 series power supplies',
    'long_description': '# BK Precision 1900\n\n## Description\n\nThis project implements the BK Precision 1902B control as a Python context manager. It allows users to easily access and manipulate the BK Precision 1902B control through a Python interface. It is only tested with the BK 1902B Power supply but should work with all of any supply for the 1900 series.\n\n## Installation\n\n### Via pip\n\nTo install the package from PyPI using pip, run the following command:\n\npip install bk_precision_1900\n\n### From the repository\n\nTo install the package from the repository, clone the repository and install it using poetry:\n\n```bash\ngit clone https://github.com/DephyInc/bk_precision_1900\ncd bk_precision_1900\npoetry install\n```\n\n## Running the Demo Code\n\nTo run the demo code, use the following command:\n\n```bash\npoetry run python bk_demo.py [SERIAL_PORT]\n```\n\nThis will execute the `bk_demo.py` script, which sets a series of voltages in the BK Precision 1902B and prints out the display readouts.\n\nNote that you will need to have poetry installed on your system in order to use the poetry run command. You can install poetry by following the instructions at https://python-poetry.org/docs/.\n',
    'author': 'Carlos Asmat',
    'author_email': 'casmat@dephy.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DephyInc/bk_precision_1900',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
