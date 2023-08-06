# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_bfchat']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.2.0,<3.0.0',
 'nonebot-plugin-htmlrender>=0.2.0.1,<0.3.0.0',
 'nonebot2>=2.0.0rc2,<3.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-bfchat',
    'version': '0.2.1',
    'description': 'A battlefield 1/v chatbot based on nonebot2 framework',
    'long_description': '<div align="center">xdm, you V ma?</div>\n\n# nonebot-plugin-bfchat\n\n一个基于nonebot2平台的战地1/5聊天机器人，提供战绩查询，群账号绑定，服务器查询等功能，提供基于[htmlrender插件](https://github.com/kexue-z/nonebot-plugin-htmlrender)渲染的美观输出。\n\n## 安装\n\nnb-cli: (推荐)(等发布)\n\n```bash\nnb plugin install nonebot-plugin-bfchat\n```\n\npip: (需要在pyproject.toml手动导入)\n\n```bash\npip install nonebot-plugin-bfchat\n```\n\n\n## 配置项及默认值\n\n```properties\nbfchat_prefix = "/"    # bfchat的命令前缀，默认为"/"\nbfchat_dir = "./bfchat_data"    # bfchat的存储目录，用于存储群绑定玩家数据\n```\n\n## 命令列表\n\n使用以下命令前均需要添加配置好的前缀\n\n| 命令                                                      | 作用                                                                                                   | 备注                                                                         |\n| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |\n| `bf help`                                               | 返回本列表                                                                                             |                                                                              |\n| `bf init`                                               | 初始化本群绑定功能，未初始化的群，群员不能使用绑定功能                                                 | 仅SUPERUSER和群管理员有效                                                    |\n| `bf1 [玩家id]`<br />`bfv [玩家id]`                    | 查询 `[玩家id]`的bf1/bfv战绩信息                                                                     | 如果查询玩家是me，则会将数据保存至本地<br />且一小时内再次查询不会再发起请求 |\n| `bf1 [玩家id] weapons`<br />`bfv\xa0[玩家id] weapons`   | 查询 `[玩家id]`的bf1/bfv武器信息                                                                     |                                                                              |\n| `bf1 [玩家id] vehicles`<br />`bfv\xa0[玩家id] vehicles` | 查询 `[玩家id]`的bf1/bfv载具信息                                                                     |                                                                              |\n| `bf1 bind [玩家id]`<br />`bfv bind [玩家id]`          | 将 对应游戏的 `[玩家id]`与命令发送人绑定，绑定后可使用 `me `代替 `[玩家id]`<br />例如 `bfv me` | bf1与bfv绑定不互通                                                           |\n| `bf1 list`<br />`bfv list`                            | 列出该服务器所有已绑定的bf1/bfv玩家信息                                                                | 使用本地数据，不会自动更新                                                   |\n| `bf1 server [服务器名]`<br />`bfv server [服务器名]`  | 查询名字包含 `[服务器名]`的bf1/bfv服务器                                                             |                                                                              |\n\n## 示例\n\nbfv me\n\n<img src="https://raw.githubusercontent.com/050644zf/nonebot-plugin-bfchat/master/img/bfvme.jpg" width="400px"/>\n\nbfv server BFV ROBOT\n\n![img](https://raw.githubusercontent.com/050644zf/nonebot-plugin-bfchat/master/img/server.png)\n\nbfv list\n\n![img](https://raw.githubusercontent.com/050644zf/nonebot-plugin-bfchat/master/img/bflist.png)\n',
    'author': 'Nightsky',
    'author_email': '050644zf@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
