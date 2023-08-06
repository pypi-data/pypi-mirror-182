# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prpc_python']

package_data = \
{'': ['*']}

install_requires = \
['setuptools>=62.0.0,<63.0.0']

extras_require = \
{'cli': ['click>=8.1.3,<9.0.0',
         'click-log>=0.4.0,<0.5.0',
         'rich>=12.6.0,<13.0.0'],
 'flask': ['flask>=2.2.2,<3.0.0', 'flask-cors>=3.0.10,<4.0.0'],
 'simple': ['click>=8.1.3,<9.0.0',
            'click-log>=0.4.0,<0.5.0',
            'rich>=12.6.0,<13.0.0',
            'flask>=2.2.2,<3.0.0',
            'flask-cors>=3.0.10,<4.0.0']}

entry_points = \
{'console_scripts': ['prpc = prpc_python.cli:prpc'],
 'prpc_python': ['sample = prpc_python.sample:app']}

setup_kwargs = {
    'name': 'prpc-python',
    'version': '0.9.0',
    'description': 'A very simple RPC-like library to make writing Pyodide applications easier. At the core of the library is a simple App + Decorator based approach inspired by Flask.',
    'long_description': '',
    'author': 'Kaj Siebert',
    'author_email': 'kaj@k-si.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SocialFinanceDigitalLabs/prpc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
