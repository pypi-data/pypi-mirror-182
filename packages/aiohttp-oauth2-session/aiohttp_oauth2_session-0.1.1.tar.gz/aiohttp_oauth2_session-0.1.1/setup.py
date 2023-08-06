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
    'version': '0.1.1',
    'description': 'A fully typed, package that adds OAuth2 support for aiohttp.ClientSession.',
    'long_description': '# aiohttp-oauth2-session\n\nA fully typed package that adds OAuth2 support for aiohttp.ClientSession.\n\n## Installation\n\n```bash\npip install aiohttp-oauth2-session\n```\n\n## Basic Usage\n\n```python\nfrom aiohttp_oauth2_session import OAuth2Session\n```\n\nYou can create a session with or without a token already known.\n\n```python\ntoken = {\n    "access_token": "abc1234",\n    "token_type": "Bearer",\n    "expires_in": 3600,\n    "refresh_token": "def5678",\n}\n\nsession = OAuth2Session(\n    client_id="client_id",\n    client_secret="client_secret",\n    redirect_uri="https://example.com/oauth/redirect",\n    scope="scope1 scope2",\n    token=token,\n)\n\n# Which allows you to make authenticated requests straight away.\nresp = await session.get("https://example.com/api/resource")\nawait session.close()\n```\n\nYou can also create a session without a token and fetch one later.\n\n```python\nsession = OAuth2Session(\n    client_id="client_id",\n    client_secret="client_secret",\n    redirect_uri="https://example.com/oauth/redirect",\n    scope="scope1 scope2",\n)\n\nawait session.fetch_token(\n    token_url="https://example.com/oauth/token",\n    authorization_response="https://example.com/oauth/redirect?code=abc1234",\n)\n\n# now you can make authenticated requests.\nresp = await session.get("https://example.com/api/resource")\nawait session.close()\n```\n\nYou can also use context managers to automatically close the session.\n\n```python\nasync with OAuth2Session(\n    client_id="client_id",\n    client_secret="client_secret",\n    redirect_uri="https://example.com/oauth/redirect",\n    scope="scope1 scope2",\n) as session:\n    await session.fetch_token(\n        token_url="https://example.com/oauth/token",\n        authorization_response="https://example.com/oauth/redirect?code=abc1234",\n    )\n    async with session.get("https://example.com/api/resource") as resp:\n        print(await resp.json())\n```\n\n## Feel free to contribute!\n\nWhat still needs to be done:\n\n- [ ] Add more comprehensive tests\n- [ ] Add typed support for other aiohttp client sessions\n- [ ] Expand the depency versions to be less restrictive\n- [ ] Make the code more readable, it\'s a bit messy right now\n- [ ] Whatever else you can think of. Please do open an issue or PR!\n\n---\n\nThis package is based on [a gist](https://gist.github.com/kellerza/5ca798f49983bb702bc6e7a05ba53def) by [kellerza](https://gist.github.com/kellerza). Thank you very much!\n',
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
