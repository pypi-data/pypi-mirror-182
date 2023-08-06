# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp_oauth2_session']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0', 'oauthlib>=3.2.2,<4.0.0']

setup_kwargs = {
    'name': 'aiohttp-oauth2-session',
    'version': '0.1.0',
    'description': 'A small package that adds OAuth2 support for aiohttp.ClientSession.',
    'long_description': '# aiohttp-oauth2-session\n\nA small package that adds OAuth2 support for aiohttp.ClientSession.\n\nMore information will be added soon.\n',
    'author': 'Cikmo',
    'author_email': '59421913+Cikmo@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Cikmo/OAuth2Session',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
