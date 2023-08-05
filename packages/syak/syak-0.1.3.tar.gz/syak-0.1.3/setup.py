# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['syak']
install_requires = \
['markdown2>=2.4.6,<3.0.0',
 'pandas>=1.5.2,<2.0.0',
 'psutil>=5.9.0,<6.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['syak = syak:main']}

setup_kwargs = {
    'name': 'syak',
    'version': '0.1.3',
    'description': 'SiYuan sync to Anki',
    'long_description': 'SYAK:同步SiYuan内容块到Anki, 自动更新, 自动删除\n\n# Prerequisite\n\n1. Anki 需要安装 AnkiConnect 插件, code 为 `2055492159`\u200b, 默认端口 `8765`\u200b\n2. 支持 Python 3.9 以上版本\n3. SiYuan 默认端口为 `6806`\u200b\n\n# Install\n\n```\npip install syak\n```\n\n# Useage\n\n1. 新建一个 `card`\u200b \u200b文档块, 名字支持前后缀, 例如 `@card`\u200b\u200b\n2. 在需要制卡的内容块后面引用 `card`\u200b \u200b文档块\n3. 制卡内容块为某个容器块下的叶子块时, 卡片正面为制卡内容块, 背面为整个容器块\n4. 制卡内容块为文档块下的叶子块时, 卡片正面和背面都是制卡内容块\n5. 运行命令 `syak -p SiYuan数据根路径(data目录的上一级)`\u200b \u200b即可同步\n6. 查看更多选项运行 `syak -h`\u200b\u200b\n\n# DEMO\n\n\u200b![demo](demo.gif)\u200b\n\n# Feature\n\n1. 自动更新, SiYuan更新内容块后, Anki自动更新\n2. 自动删除, 删除`card`\u200b引用块, Anki自动删除\n3. 根据文档块层级自动建立 deck 层级\n4. 支持 media 文件\n5. 自动删除 empty deck\n\n# Not Support\n\n1. Close\n2. 代码块高亮\n3. 超级块未适配\n\n# MORE\n\n使用带有定时运行脚本功能的软件,如`Keyboard Maestro`\u200b或者`Quicker`\u200b实现后台无缝同步',
    'author': 'why8023',
    'author_email': 'whyniaaa@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
