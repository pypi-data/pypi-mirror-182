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
{'console_scripts': ['prpc = prpc_python.cli:prpc']}

setup_kwargs = {
    'name': 'prpc-python',
    'version': '0.9.1',
    'description': 'A very simple RPC-like library to make writing Pyodide applications easier. At the core of the library is a simple App + Decorator based approach inspired by Flask.',
    'long_description': '\n# prpc-python - Pyodide Remote Procedure Calls - Python Server\n\n[![PyPI version](https://badge.fury.io/py/prpc-python.svg)](https://badge.fury.io/py/prpc-python)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/prpc-python.svg)](https://pypi.org/project/prpc-python/)\n[![PyPI - License](https://img.shields.io/pypi/l/prpc-python.svg)](https://pypi.org/project/prpc-python/)\n[![GitHub issues](https://img.shields.io/github/issues/SocialFinanceDigitalLabs/prpc.svg)](https://github.com/SocialFinanceDigitalLabs/prpc/issues)\n\nProvides server-side bindings for [prpc][prpc] API. \n\nTo expose a python function as a prpc method you first create\na prpc `RpcApp` and then decorate your function with `@app.call`. \n\nCreate a file called `myapp.py` and add the following code:\n\n```python\n# myapp.py\nfrom prpc_python import RpcApp\n\napp = RpcApp("Sample App")\n\n\n@app.call\ndef hello() :\n    return "World"\n```\n\n## Discovering your API\n\nYou can now discover your API using the `prpc` command line tool. To do this\nyou either have to specify the plugin ID of your app or "publish" the\nplugin using the Python [plugin discovery][discovery] approach.\n\nThe ID of your plugin is the name of the module containing \nyour `RpcApp` instance plus the name of the instance, e.g. \n`myapp:app` for the example above.\n\nYou can now use the command line tool to discover your API:\n\n```bash\nprpc commands -a myapp:app     \n```\n\nand you can even call your function from the command line:\n\n```bash\nprpc run -a myapp:app hello\n```\n\n## Publishing \n\nYou don\'t always want to have to specify the plugin ID of your app. You can \nuse the approach described in the [metadata][discovery] section of the packaging\nspec to publish your plugin. If you have a `pyproject.toml` file, then add\nthe following section:\n\n```toml\n[tool.poetry.plugins."prpc_python"]\nmyapp = "myapp:app"\n```\n\nIf your plugin is the only one in your installed dependencies, then it will\nbe automatically chosen, and you can omit the `-a myapp:app` argument.\n\n## Files\n\nprpc also supports file transfers. If you receive a file from the remote \nendpoint, you will receive a `prpc_python.RemoteFile` object. This object\nhas a standard `read` method, so you can use it as a file-like object.\n\nIt may also have `filename`, `size` and `content_type` attributes but it\ndepends on the source of the file whether these are available.\n\n[prpc]: https://github.com/SocialFinanceDigitalLabs/prpc\n[discovery]: https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/#using-package-metadata    \n',
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
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
