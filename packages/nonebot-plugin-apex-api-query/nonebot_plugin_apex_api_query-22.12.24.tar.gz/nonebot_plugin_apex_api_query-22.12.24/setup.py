# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_apex_api_query']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot2>=2.0.0rc1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-apex-api-query',
    'version': '22.12.24',
    'description': '基于 NoneBot2 的 Apex Legends API 查询插件',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# nonebot-plugin-apex-api-query\n\n*✨ NoneBot Apex Legends API 查询插件 ✨*\n\n![GitHub](https://img.shields.io/github/license/H-xiaoH/nonebot-plugin-apex-api-query)\n![PyPI](https://img.shields.io/pypi/v/nonebot-plugin-apex-api-query)\n\n</div>\n\n## 使用方法\n在您的 NoneBot 配置文件中写入 `apex_api_key` 值。\n例如: `apex_api_key=YOUR_API_KEY`\n\n您可以点击 [此处](https://portal.apexlegendsapi.com/) 申请 API 密钥。\n\n在与 Bot 私聊 或 已加入的群聊 中发送命令。\n\n### 查询玩家信息\n`/bridge [玩家名称]` 、\n`/玩家 [玩家名称]`、\n`/uid [玩家UID]`、\n`/UID [玩家UID]`\n\n暂不支持除 PC 外的平台查询。\n\n输出示例：\n```text\n玩家信息:\n名称: HxiaoH\nUID: 1002727553409\n平台: PC\n等级: 256\n距下一级百分比: 86%\n封禁状态: 否\n剩余秒数: 0\n最后封禁原因: 竞技逃跑冷却\n大逃杀分数: 10418\n大逃杀段位: 白金 2\n竞技场分数: 2317\n竞技场段位: 白银 3\n大厅状态: 打开\n在线: 是\n游戏中: 是\n可加入: 是\n群满员: 否\n已选传奇: 寻血猎犬\n当前状态: 比赛中\n```\n\n### 查询大逃杀地图轮换\n`/maprotation` 、 `/地图`\n\n输出示例：\n```text\n大逃杀:\n当前地图: 世界尽头\n下个地图: 破碎月亮\n剩余时间: 00:43:15\n\n竞技场:\n当前地图: 相位穿梭器\n下个地图: 栖息地 4\n剩余时间: 00:13:15\n\n排位赛联盟:\n当前地图: 破碎月亮\n下个地图: 奥林匹斯\n剩余时间: 599:43:15\n\n排位竞技场:\n当前地图: 相位穿梭器\n下个地图: 栖息地 4\n剩余时间: 00:13:15\n```\n\n### 查询猎杀者信息\n`/predator` 、 `/猎杀`\n\n输出示例：\n```text\n大逃杀:\nPC 端:\n顶尖猎杀者人数: 750\n顶尖猎杀者分数: 34176\n顶尖猎杀者UID: 1008992986436\n大师和顶尖猎杀者人数: 20995\nPS4/5 端:\n顶尖猎杀者人数: 752\n顶尖猎杀者分数: 25039\n顶尖猎杀者UID: 6655163505495496802\n大师和顶尖猎杀者人数: 7382\nXbox 端:\n顶尖猎杀者人数: 750\n顶尖猎杀者分数: 20262\n顶尖猎杀者UID: 2535442891191517\n大师和顶尖猎杀者人数: 2947\nSwitch 端:\n顶尖猎杀者人数: -1\n顶尖猎杀者分数: 15000\n顶尖猎杀者UID: -1\n大师和顶尖猎杀者人数: 671\n\n竞技场:\nPC 端:\n顶尖猎杀者人数: 750\n顶尖猎杀者分数: 9735\n顶尖猎杀者UID: 1010770350454\n大师和顶尖猎杀者人数: 2919\nPS4/5 端:\n顶尖猎杀者人数: 749\n顶尖猎杀者分数: 10279\n顶尖猎杀者UID: 5266195274595015901\n大师和顶尖猎杀者人数: 5226\nXbox 端:\n顶尖猎杀者人数: 751\n顶尖猎杀者分数: 8578\n顶尖猎杀者UID: 2535421772058188\n大师和顶尖猎杀者人数: 1821\nSwitch 端:\n顶尖猎杀者人数: -1\n顶尖猎杀者分数: 8000\n顶尖猎杀者UID: -1\n大师和顶尖猎杀者人数: 291\n```\n\n### 查询复制器轮换\n`/crafting` 、 `/制造`\n\n输出示例：\n```text\n每日制造:\n4 倍至 8 倍可调节式狙击手 等级3 35 点\n加长狙击弹匣 等级3 35 点\n\n每周制造:\n击倒护盾 等级3 30 点\n移动重生信标 等级2 50 点\n\n赛季制造:\n和平捍卫者 等级1 30 点\n喷火轻机枪 等级1 30 点\n```\n\n### 订阅制造/地图轮换\n`/subcraft`、`/订阅制造`\n`/submap`、`/订阅地图`\n`/unsubcraft`、`/取消订阅制造`\n`/unsubmap`、`/取消地图制造`\n\n每日 2 时自动查询制造轮换\n每时自动查询地图轮换\n',
    'author': 'HxiaoH',
    'author_email': '412454922@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/H-xiaoH/nonebot-plugin-apex-api-query',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
