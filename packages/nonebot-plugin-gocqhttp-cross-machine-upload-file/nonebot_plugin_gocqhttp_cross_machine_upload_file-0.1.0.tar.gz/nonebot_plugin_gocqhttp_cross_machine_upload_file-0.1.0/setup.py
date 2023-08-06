# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nonebot_plugin_gocqhttp_cross_machine_upload_file']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=5.2.0,<6.0.0',
 'nonebot-adapter-onebot>=2.1.5,<3.0.0',
 'nonebot2>=2.0.0rc1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-gocqhttp-cross-machine-upload-file',
    'version': '0.1.0',
    'description': '',
    'long_description': 'nonebot-plugin-gocqhttp-cross-machine-upload-file\n========\n\n为go-cqhttp与nonebot部署于不同机器的系统提供上传群文件、私聊文件的能力。\n\n## 配置\n\n### callback_host\n\n回调HOST，设置为nonebot所在的主机名/IP。务必保证go-cqhttp所在主机可访问，用于让go-cqhttp下载本机文件。\n\n默认值：127.0.0.1\n\n### callback_port\n\n回调端口，保持默认值即可。\n\n默认值：与PORT保持一致即可',
    'author': 'ssttkkl',
    'author_email': 'huang.wen.long@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
