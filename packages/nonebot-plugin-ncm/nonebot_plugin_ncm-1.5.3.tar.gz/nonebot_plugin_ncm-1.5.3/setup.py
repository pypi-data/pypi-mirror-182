# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot-plugin-ncm']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'aiofile>=3.7.4,<4.0.0',
 'httpx>=0.23.1,<0.24.0',
 'nonebot-adapter-onebot>=2.1.5,<3.0.0',
 'nonebot2>=2.0.0rc2,<3.0.0',
 'pyncm>=1.6.8.3,<2.0.0.0',
 'qrcode>=7.3.1,<8.0.0',
 'tinydb>=4.7.0,<5.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ncm',
    'version': '1.5.3',
    'description': '基于go-cqhttp与nonebot2的 网易云 无损音乐下载',
    'long_description': '\n\n<p align="center">\n  <img src="https://files.catbox.moe/7cy61g.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# nonebot-plugin-ncm\n\n✨ 基于go-cqhttp与nonebot2的 网易云 无损音乐 点歌/下载 ✨\n</div>\n\n<p align="center">\n  <a href="https://github.com/kitUIN/nonebot-plugin-ncm/blob/master/LICENSE">\n    <img src="https://img.shields.io/badge/license-Apache--2.0-green" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-ncm">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-ncm" alt="pypi">\n  </a>\n  <a href="https://github.com/nonebot/nonebot2/releases/tag/v2.0.0rc2">\n    <img src="https://img.shields.io/static/v1?label=nonebot2&message=v2.0.0rc2&color=brightgreen" alt="nonebot">\n  </a>\n  <a href="https://github.com/kitUIN/nonebot-plugin-ncm/releases">\n    <img src="https://img.shields.io/github/v/release/kitUIN/nonebot-plugin-ncm" alt="release">\n  </a>\n  <a href="https://wakatime.com/badge/user/3b5608c7-e0b6-44a2-a217-cad786040b48/project/2a431792-e82f-48f5-839c-9ee566910fe5"><img src="https://wakatime.com/badge/user/3b5608c7-e0b6-44a2-a217-cad786040b48/project/2a431792-e82f-48f5-839c-9ee566910fe5.svg" alt="wakatime"></a>\n</p>\n\n\n## 安装\n### 使用pip安装\n1.`pip install nonebot-plugin-ncm` 进行安装  \n2.并在`bot.py`添加`nonebot.load_plugin(\'nonebot-plugin-ncm\')`\n### 使用nb-cli安装(推荐)\n`nb plugin install nonebot-plugin-ncm` 进行安装\n\n<details>\n  <summary>如果希望使用`nonebot2 a16`及以下版本 </summary>\n  请使用`pip install nonebot-plugin-ncm==1.1.0`进行安装\n</details>\n\n## 升级\n1.`pip install nonebot-plugin-ncm --upgrade` 进行升级  \n2. 低于`1.5.0`版本升级请删除`db`文件夹内`ncm`开头文件  \n3. 根据新的`config`项配置`.env`文件\n## 快速使用\n将链接或者卡片分享到聊天群或机器人,回复分享的消息并输入`下载`即可进行下载  \n**默认下载状态为关闭，请在每个群内使用`/ncm t`开启,私聊则默认开启**\n![img](https://files.catbox.moe/g7c230.png)\n### 命令列表：\n| 命令                 | 备注        |\n|--------------------|-----------|\n| /ncm               | 获取命令菜单    |\n| /ncm t             | 开启下载      |\n| /ncm f             | 关闭下载      |\n| /ncm search t      | 开启点歌      |\n| /ncm search f      | 关闭点歌      |\n| /点歌 歌名             | 点歌        |\n| /ncm private qq号 t | 开启该用户私聊下载 |\n| /ncm private qq号 f | 关闭该用户私聊下载 |\n- 命令开始符号会自动识别[`COMMAND_START`](https://v2.nonebot.dev/docs/api/config#Config-command_start)项\n\n## 注意说明\n- 使用的网易云账号**需要拥有黑胶VIP** \n- 默认下载最高音质的音乐 \n- 本程序实质为调用web接口下载音乐上传  \n\n## 配置文件说明\n```\nncm_admin_level=1 # 设置命令权限(1:仅限superusers和群主,2:在1的基础上+管理员,3:所有用户)\nncm_ctcode="86" # 手机号区域码,默认86\nncm_phone=  # 手机登录\nncm_password=  # 密码\nncm_playlist_zip=False # 上传歌单时是否压缩\n```\n\n## 功能列表\n- [x] 识别/下载 网易云单曲\n    - 链接\n    - 卡片\n    - 卡片转发\n- [x] 识别/下载 网易云歌单    \n    - 链接\n    - 卡片\n    - 卡片转发\n- [x] 点歌(网易云)\n- [ ] QQ音乐无损下载\n\n# 鸣谢\n- [pyncm](https://github.com/greats3an/pyncm)\n- [nonebot2](https://github.com/nonebot/nonebot2)\n',
    'author': 'kitUIN',
    'author_email': 'kulujun@gmail.com',
    'maintainer': 'kitUIN',
    'maintainer_email': 'kulujun@gmail.com',
    'url': 'https://github.com/kitUIN/nonebot-plugin-ncm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
