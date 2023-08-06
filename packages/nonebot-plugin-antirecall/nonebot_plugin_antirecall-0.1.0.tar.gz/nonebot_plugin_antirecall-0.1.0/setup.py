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
    'version': '0.1.0',
    'description': 'Anti-recall plugin for QQbot in Nonebot2',
    'long_description': '# nonebot_plugin_anti-recall\nAnti-recall plugin for QQ in Nonebot2',
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
