# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

modules = \
['nonebot_plugin_no_repeat']
install_requires = \
['nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-no-repeat',
    'version': '0.0.1',
    'description': '不要复读',
    'long_description': '<div align="center">\n\n# nonebot_plugin_no_repeat 不要复读\n\n防止代码炸了在群里复读刷屏，让你写插件的时候更安全\n\n</div>\n\n## 配置（可选）\n\n| 名称                | 值             | 意义                                                | 默认值/推荐值 |\n| ------------------- | -------------- | --------------------------------------------------- | ------------- |\n| no_repeat_mode      | use, not_use   | 白名单模式(use) or 黑名单模式(not_use)              | not_use       |\n| no_repeat_groups    | [12345, 23456] | 群聊号                                              | []            |\n| no_repeat_threshold | 3              | 发送重复语句达到3条后视为复读（第三条会被阻止发送） | 3             |\n| no_repeat_gap       | 20             | 与上一条语句的发送间隔超过20s则不视为复读           | 20            |\n\n\n白名单模式：仅在指定群内开启该功能\n\n黑名单模式：仅在指定群内关闭该功能（比如你的机器人专用调试群），其他群均开启该功能\n\n## 实现原理\n\nhttps://v2.nonebot.dev/docs/next/advanced/runtime-hook#bot-api-%E8%B0%83%E7%94%A8%E9%92%A9%E5%AD%90\n\n检测到异常复读情况后抛出`MockApiException`\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-no-repeat',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
