# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['barsdiary']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'pydantic>=1.10.2,<2.0.0']

extras_require = \
{'async': ['aiohttp>=3.8.3,<4.0.0'], 'sync': ['httpx>=0.23.1,<0.24.0']}

setup_kwargs = {
    'name': 'barsdiary',
    'version': '0.1.3',
    'description': 'Python library for working with API "БАРС.Web-Образование"',
    'long_description': 'Тестовый запуск. ',
    'author': 'mironovmeow',
    'author_email': '71277890+mironovmeow@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mironovmeow/barsdiary',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
