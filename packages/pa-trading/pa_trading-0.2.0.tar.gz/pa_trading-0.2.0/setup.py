# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pa_trading', 'pa_trading._pb']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['pa = pa_trading.pa:cli']}

setup_kwargs = {
    'name': 'pa-trading',
    'version': '0.2.0',
    'description': 'Comandos para cálculos price action - tool kit de comandos',
    'long_description': '',
    'author': 'Valmir Franca',
    'author_email': 'vfranca3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
