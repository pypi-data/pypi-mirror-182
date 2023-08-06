# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aworda',
 'aworda.rainfer',
 'aworda.rainfer.adapter',
 'aworda.rainfer.entry',
 'aworda.rainfer.event',
 'aworda.rainfer.message',
 'aworda.rainfer.message.commander',
 'aworda.rainfer.message.parser',
 'aworda.rainfer.util']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0',
 'graia-broadcast>=0.16.1,<0.17.0',
 'loguru>=0.6,<0.7',
 'pydantic>=1.8.2,<2.0.0',
 'typing-extensions>=4.0,<5.0',
 'yarl>=1.7,<2.0']

extras_require = \
{':extra == "graia" or extra == "standard" or extra == "full"': ['graia-saya>=0.0,<0.1'],
 'full': ['graia-scheduler>=0.0,<0.1',
          'fastapi>=0.74.1,<1.0.0',
          'uvicorn[standard]>=0.17.5,<0.18.0',
          'prompt-toolkit>=3.0.24,<4.0.0'],
 'graia': ['graia-scheduler>=0.0,<0.1'],
 'server': ['fastapi>=0.74.1,<1.0.0', 'uvicorn[standard]>=0.17.5,<0.18.0'],
 'standard': ['graia-scheduler>=0.0,<0.1', 'prompt-toolkit>=3.0.24,<4.0.0']}

setup_kwargs = {
    'name': 'aworda-rainfer',
    'version': '0.0.1',
    'description': 'Modified from Ariadne & Another elegant Python QQ Bot framework for mirai and mirai-api-http v2.',
    'long_description': '<div align="center">\n\n# Rainfer\n\n_Modified from Ariadne & Another elegant Python QQ Bot framework for mirai and mirai-api-http v2._\n\n> 希望落空时间\n\n<a href="https://pypi.org/project/graia-ariadne"><img alt="PyPI" src="https://img.shields.io/pypi/v/aworda-rainfer" /></a></td>\n<a href="https://pypi.org/project/graia-ariadne"><img alt="PyPI Pre Release" src="https://img.shields.io/github/v/tag/AwordaProject/Rainfer?include_prereleases&label=latest&color=orange"></td>\n<a href="https://pypi.org/project/graia-ariadne"><img alt="Python Version" src="https://img.shields.io/pypi/pyversions/aworda-rainfer" /></a>\n<a href="https://pypi.org/project/graia-ariadne"><img alt="Python Implementation" src="https://img.shields.io/pypi/implementation/aworda-rainfer"></a>\n<a href="https://nodocs.lol"><img alt="docs" src="https://img.shields.io/badge/文档-here-blue" /></a>\n<a href="https://nodocs.lol"><img alt="API docs" src="https://img.shields.io/badge/API_文档-here-purple"></a>\n<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-black.svg" alt="black" /></a>\n<a href="https://pycqa.github.io/isort/"><img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat" alt="isort"/></a>\n<a href="https://github.com/AwordaProject/Rainfer/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/github/license/GraiaProject/Rainfer"></a>\n\n</div>\n\n**本项目适用于 mirai-api-http 2.0 以上版本**.\n\nRainfer 是 修改自 `Graia Project`  [`Ariadne`](https://github.com/GraiaProject/Ariadne) 0.6.16 的一个很烂活\n\nAriadne 是很好的项目，拥有广阔的未来，本框架就不要用了，去用 Ariadne 吧，\n\n之后随着 GraiaProject 的不断开发迭代， Ariadne将会支持更多平台并拥有 module Market Place\n\n**注意, 本框架需要 [`mirai-api-http v2`](https://github.com/project-mirai/mirai-api-http).**\n\n## 安装\n\n`poetry add aworda-rainfer`\n\n或\n\n`pip install aworda-rainfer`\n\n> 我们强烈建议使用 [`poetry`](https://python-poetry.org) 进行包管理\n\n## 开始使用\n\n```python\nfrom aworda.rainfer.app import Rainfer\nfrom aworda.rainfer.message.chainx import MessageChainX\nfrom aworda.rainfer.message.element import Plain\nfrom aworda.rainfer.model import Friend, MiraiSession\n\napp = Rainfer(MiraiSession(host="http://localhost:8080", verify_key="ServiceVerifyKey", account=123456789))\n\n\n@app.broadcast.receiver("FriendMessage")\nasync def friend_message_listener(app: Rainfer, friend: Friend):\n    await app.sendMessage(friend, MessageChain.Plain("Hello, World!"))\n\n\napp.launch_blocking()\n```\n\nThanks for your reading ~\n',
    'author': 'LinNian',
    'author_email': 'crynian@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AwordaProject/Rainfer',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
