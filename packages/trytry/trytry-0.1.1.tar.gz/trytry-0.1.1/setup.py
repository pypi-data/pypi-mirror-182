# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['trytry']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'trytry',
    'version': '0.1.1',
    'description': '优雅地处理python异常',
    'long_description': '# TryTry\n<a href="https://pypi.org/project/trytry" target="_blank">\n    <img src="https://img.shields.io/pypi/v/trytry.svg" alt="Package version">\n</a>\n\n<a href="https://pypi.org/project/trytry" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/trytry.svg" alt="Supported Python versions">\n</a>\n\n[中文文档](README_ZH.md)\n\n\n## install\n\n```bash\npip install trytry\n```\n\n## Example\n\n### handle exception\n\n```python\nfrom trytry import trytry\n\n\n@trytry\ndef my_function():\n    raise FileNotFoundError(\'file not found\')\n\n\n@trytry\ndef my_function2():\n    print(1 / 0)\n\n\n@trytry.exception(ZeroDivisionError)\ndef handle_zero_division_error(func, e):\n    print(func.__name__, str(e))\n\n\n@trytry.exception(FileNotFoundError)\ndef handle_file_not_found_error(func, e):\n    print(func.__name__, str(e))\n\n\nif __name__ == \'__main__\':\n    my_function()\n    my_function2()\n```\n\n\n### handle all exception\n\n```python\nfrom trytry import trytry\n\n\n@trytry\ndef my_function():\n    raise FileNotFoundError(\'file not found\')\n\n\n@trytry\ndef my_function2():\n    print(1 / 0)\n\n\n@trytry.exception(Exception)\ndef handle_all_error(func, e):\n    print(func.__name__, str(e))\n\n\nif __name__ == \'__main__\':\n    my_function()\n    my_function2()\n```\n\nAll of the above exceptions are caught and are global exceptions. \nYou can also catch exceptions for specific functions.\n```python\nfrom trytry import trytry\n\n\n@trytry\ndef my_function():\n    print(1 / 0)\n\n@my_function.exception(ZeroDivisionError)\ndef handle_zero_division_error(func, e):\n    print(func.__name__, str(e))\n```\n',
    'author': 'miclon',
    'author_email': 'jcnd@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
