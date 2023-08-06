# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_antirecall']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.4,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-antirecall',
    'version': '0.1.3',
    'description': 'Anti-recall plugin for QQbot in Nonebot2',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-antirecall\n\n_✨ NoneBot 防撤回插件 ✨_\n\n\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/A-kirami/nonebot-plugin-namelist.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-namelist">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-namelist.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n\n</div>\n\n\n## 📖 介绍\n\n经过多次修改稍微复杂点的防撤回插件\n\n-> 更新后可能要删掉bot目录下\\data\\enablelist 文件夹内的配置文件,并重新设置\n\n开启后群内撤回消息会被bot发送\n\n群主可以开关本群的防撤回\n\n不建议使用私聊功能,容易风控(建议收购企鹅🐧)\n\n超级用户可以开启一个群,每次有撤回消息会在群内通知,这样不用多次私聊转发,群内消息减小企鹅风控\n\n超级用户可以查看全局防撤回和列表。\n\n## 💿 安装\n\n<details>\n<summary>使用 nb-cli 安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n    nb plugin install nonebot-plugin-antirecall\n\n</details>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n    pip install nonebot-plugin-antirecall\n</details>\n<details>\n<summary>pdm</summary>\n\n    pdm add nonebot-plugin-antirecall\n</details>\n<details>\n<summary>poetry</summary>\n\n    poetry add nonebot-plugin-antirecall\n</details>\n<details>\n<summary>conda</summary>\n\n    conda install nonebot-plugin-antirecall\n</details>\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'nonebot_plugin_antirecall\')\n\n</details>\n\n\n## 🎉 使用\n### 指令表\n| 指令 | 说明 |\n|:-----:|:----:|\n| 开启/添加防撤回, enable + 群号1 群号2 ...|开启群的防撤回 |\n| 关闭/删除防撤回, disable + 群号1 群号2 ...|关闭群的防撤回 |\n| 查看防撤回群聊 |查看防撤回群聊 |\n| 开启/关闭绕过管理层 |管理员/群主不会被防撤回,仅限群内 |\n| 防撤回菜单 |打开本插件菜单 |\n| 开启/关闭防撤回私聊gid uid |超级管理员私聊使用,gid群号的群撤回消息会私聊给uid的用户,如果群没开启防撤回就不生效 |\n| 查看防撤回私聊 |查看私聊列表,私聊使用,会返回json数据.|\n| 开启防撤回私聊 gid |设置防撤回触发后监听的群,一个参数群号(ps.仅限一个群[建议是一个私人小群专门用来干这事]重新设置会覆盖)|\n| 关闭防撤回私聊 |无参数,删除这个监听群,不监听 |\n| 查看防撤回监听 |查看监听的群和发送的群,一个json |\n| 添加/删除防撤回监听 gid|添加防撤回被监听的群,一次一个[不建议太多,会风控]|\n\nTips防撤回的英文指令 : enable/disable, enable/disable here, bypass/no bypass here, clear list, antirecall menu, enable/disable private msg, enable/disable/add/remove/view listener, list private msg\n',
    'author': 'Jerry',
    'author_email': 'jerry080801@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Jerry080801/nonebot-plugin-antirecall',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
