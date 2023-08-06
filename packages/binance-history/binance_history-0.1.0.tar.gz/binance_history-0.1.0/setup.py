# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binance_history']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'binance-history',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Meng Xiangzhuo',
    'author_email': 'aumo@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
