# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['syak']
install_requires = \
['markdown2>=2.4.6,<3.0.0',
 'pandas>=1.5.2,<2.0.0',
 'psutil>=5.9.0,<6.0.0',
 'requests>=2.28.1,<3.0.0',
 'schedule>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['syak = syak:main']}

setup_kwargs = {
    'name': 'syak',
    'version': '0.1.7',
    'description': 'SiYuan sync to Anki',
    'long_description': 'SYAK:同步 SiYuan 内容块到 Anki, 自动更新, 自动删除\n\n> 如果觉得有帮助, 麻烦点个 Star⭐\n>\n\n⚠ **初次使用请提前备份 Anki, 以免数据误删!**\n\n# Prerequisite\n\n1. Anki 需要安装 AnkiConnect 插件, code 为 `2055492159`\u200b\u200b\u200b\u200b, 默认端口 `8765`\u200b\u200b\u200b\u200b\n2. 支持 Python 3.9 以上版本\n3. SiYuan 默认端口为 `6806`\u200b\u200b\u200b\u200b\n4. 同步时, 保持 SiYuan 和 Anki 同时运行\n\n# Install\n\n```\npip install -U syak\n```\n\n# Usage\n\n1. 新建一个 `card`\u200b\u200b \u200b文档块, 名字支持前后缀, 例如 `@card`\u200b\u200b\u200b\n2. 在需要制卡的内容块后面引用 `card`\u200b\u200b \u200b文档块\n3. 制卡内容块为某个容器块下的叶子块时, 卡片正面为制卡内容块, 背面为整个容器块\n4. 制卡内容块为文档块下的叶子块时, 卡片正面为制卡内容块, 背面为空\n5. 运行命令 `syak -p SiYuan数据根路径(data目录的上一级)`\u200b\u200b \u200b即可同步\n6. 运行周期任务 `syak -p SiYuan数据根路径(data目录的上一级) -i (seconds)`\u200b, 例如每 5 分钟运行一次 `syak -p SiYuan数据根路径(data目录的上一级) -i 300`\u200b\n7. 后台运行\n\n   1. Linux&macOS `nohup syak -p SiYuan数据根路径(data目录的上一级) -i (seconds) &`\u200b\n   2. Windows `start /b syak -p SiYuan数据根路径(data目录的上一级) -i (seconds)`\u200b\n8. 查看更多选项运行 `syak -h`\u200b\u200b\u200b\n\n# Demo\n\n\u200b![demo](demo.gif)\u200b\n\n# Feature\n\n1. 添加 SiYuan URL 跳转链接\n2. 自动更新, SiYuan 更新内容块后, Anki 自动更新\n3. 自动删除, 删除 `card`\u200b \u200b引用块, Anki 自动删除\n4. 根据文档块层级自动建立 deck 层级\n5. 支持 media 文件\n6. 自动删除 empty deck\n7. 同步完成时, 发送同步信息给 SiYuan, 停留 5s\n\n# Not Support (currently)\n\n1. Close\n2. 代码块语法高亮\n3. 超级块未适配\n\n# More\n\n1. macOS 用户如果遇到同步耗时较长的问题, 可以参考:\n\n   1. [FooSoft Productions - Anki-Connect](https://foosoft.net/projects/anki-connect/)\n\n      > Starting with [Mac OS X Mavericks](https://en.wikipedia.org/wiki/OS_X_Mavericks), a feature named *App Nap* has been introduced to the operating system. This feature causes certain applications which are open (but not visible) to be placed in a suspended state. As this behavior causes Anki-Connect to stop working while you have another window in the foreground, App Nap should be disabled for Anki:\n      >\n      > 1. Start the Terminal application.\n      > 2. Execute the following commands in the terminal window:\n      >\n      >    ```\n      >    defaults write net.ankiweb.dtop NSAppSleepDisabled -bool true\n      >    defaults write net.ichi2.anki NSAppSleepDisabled -bool true\n      >    defaults write org.qt-project.Qt.QtWebEngineCore NSAppSleepDisabled -bool true\n      >    ```\n      > 3. Restart Anki.\n      >\n\n\u200d',
    'author': 'why8023',
    'author_email': 'whyniaaa@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/why8023/SYAK',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
