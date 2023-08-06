# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_random_ban']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0', 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-random-ban',
    'version': '0.1.0',
    'description': '随机禁言一名群员或自己n分钟（n通过参入数字然后随机实现），简单粗暴。',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot_plugin_random_ban\n  \n_✨ NoneBot 随机禁言插件 ✨_\n  \n<a href="https://github.com/Ikaros-521/nonebot_plugin_random_ban/stargazers">\n    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Ikaros-521/nonebot_plugin_random_ban?color=%09%2300BFFF&style=flat-square">\n</a>\n<a href="https://github.com/Ikaros-521/nonebot_plugin_random_ban/issues">\n    <img alt="GitHub issues" src="https://img.shields.io/github/issues/Ikaros-521/nonebot_plugin_random_ban?color=Emerald%20green&style=flat-square">\n</a>\n<a href="https://github.com/Ikaros-521/nonebot_plugin_random_ban/network">\n    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Ikaros-521/nonebot_plugin_random_ban?color=%2300BFFF&style=flat-square">\n</a>\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/Ikaros-521/nonebot_plugin_random_ban.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot_plugin_random_ban">\n    <img src="https://img.shields.io/pypi/v/nonebot_plugin_random_ban.svg" alt="pypi">\n</a>\n<a href="https://www.python.org">\n    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n</a>\n\n</div>\n\n适用于nonebot2 v11的随机禁言一名群员或自己n分钟 插件      \n注意：需要给bot管理员才能使用。  \n\n## 🔧 开发环境\nNonebot2：2.0.0b5  \npython：3.8.13  \n操作系统：Windows10（Linux兼容性问题不大）  \n编辑器：pycharm  \n\n## 💿 安装\n\n### 1. nb-cli安装（推荐）\n\n在你bot工程的文件夹下，运行cmd（运行路径要对啊），执行nb命令安装插件，插件配置会自动添加至配置文件  \n```\nnb plugin install nonebot_plugin_random_ban\n```\n\n### 2. 本地安装\n\n将项目clone到你的机器人插件下的对应插件目录内（一般为机器人文件夹下的`src/plugins`），然后把`nonebot_plugin_random_ban`文件夹里的内容拷贝至上一级目录即可。  \nclone命令参考（得先装`git`，懂的都懂）：\n```\ngit clone https://github.com/Ikaros-521/nonebot_plugin_random_ban.git\n``` \n也可以直接下载压缩包到插件目录解压，然后同样提取`nonebot_plugin_random_ban`至上一级目录。  \n目录结构： ```你的bot/src/plugins/nonebot_plugin_random_ban/__init__.py```  \n\n\n### 3. pip安装\n\n```\npip install nonebot_plugin_random_ban\n```  \n打开 nonebot2 项目的 ```bot.py``` 文件, 在其中写入  \n```nonebot.load_plugin(\'nonebot_plugin_random_ban\')```  \n当然，如果是默认nb-cli创建的nonebot2的话，在bot路径```pyproject.toml```的```[tool.nonebot]```的```plugins```中添加```nonebot_plugin_random_ban```即可  \npyproject.toml配置例如：  \n``` \n[tool.nonebot]\nplugin_dirs = ["src/plugins"]\nplugins = ["nonebot_plugin_random_ban"]\n``` \n\n### 更新版本\n```\nnb plugin update nonebot_plugin_random_ban\n```\n\n## 🔧 配置\n\n### env配置\n```\n# nonebot_plugin_random_ban\n# 任何人都可以使用 随机禁言，开启后将会迎来至暗时刻\nanyone_can_random_ban = []\n```\n若某群想长期启动`至暗时刻`，配置参考：  \n```\n# nonebot_plugin_random_ban\n# 任何人都可以使用 随机禁言，开启后将会迎来至暗时刻\nanyone_can_random_ban = [123456, 114514]\n```\n|       配置项      | 必填 | 默认值 |             说明            |\n|:----------------:|:----:|:----:|:----------------------------:|\n| `nonebot_plugin_random_ban` | 否 | `[]` | 数组内配置开启`至暗时刻`的群号即可 |\n\n\n\n## 🎉 功能\n随机禁言一名群员或自己n分钟（n通过传入数字然后随机实现），简单粗暴。可以`开启至暗时刻`，就是所有人可以使用`随禁`命令，刺激。    \n\n## 👉 命令\n\n### 随机禁言 或 随禁\n命令结构：```/随机禁言 [最大禁言时间]``` 或 ```/随禁 [最大禁言时间]```  （最大禁言时间不填默认60分钟内的随机）  \n例如：```/随机禁言``` 或 ```/随禁 10```  \nbot返回内容：  \n```\n恭喜幸运儿:xxx 获得6分钟的禁言服务\n```\n\n### 口球 或 禁我\n命令结构：```/口球 [最大禁言时间]``` 或 ```/禁我 [最大禁言时间]```  （最大禁言时间不填默认60分钟内的随机）  \n例如：```/口球``` 或 ```/禁我 10```  \nbot返回内容：  \n```\n恭喜您获得6分钟的禁言服务\n```\n\n### 开启至暗时刻\n命令结构：```/开启至暗时刻``` 或 ```/至暗时刻启动``` 或 ```/至暗时刻开启```  或 ```/启动至暗时刻```  \n例如：```/开启至暗时刻```  \n说明：至暗时刻就是所有人可以使用 `/随禁` 命令，将是一片腥风血雨。  \nbot返回内容：  \n```\n本群开启 至暗时刻成功，开始狩猎吧！\n```\n\n### 关闭至暗时刻\n命令结构：```/关闭至暗时刻``` 或 ```/至暗时刻关闭``` 或 ```/停止至暗时刻```  或 ```/至暗时刻停止```  \n例如：```/关闭至暗时刻```  \nbot返回内容：  \n```\n本群已关闭 至暗时刻，世界恢复和平。\n```\n\n## ⚙ 拓展\n自行修改源码喵~\n\n\n## 📝 更新日志\n\n<details>\n<summary>展开/收起</summary>\n\n### 0.0.1\n\n- 插件初次发布  \n\n### 0.0.2\n\n- 补充插件元信息\n- 优化文档\n\n### 0.0.3\n\n- 新增命令 口球 或 禁我，自己禁自己\n\n### 0.0.4\n\n- 优化文档\n\n### 0.0.5\n\n- 新增可以开启任何人都使用随机禁言的配置项\n\n### 0.1.0\n\n- 新增 至暗时刻，就是所有人可以使用`随禁`命令，刺激。\n\n</details>\n\n',
    'author': 'Ikaros',
    'author_email': '327209194@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ikaros-521/nonebot_plugin_random_ban',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
