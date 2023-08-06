# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['toydl', 'toydl.torch']

package_data = \
{'': ['*']}

extras_require = \
{'full': ['tqdm>=4.0.0,<5.0.0']}

setup_kwargs = {
    'name': 'toydl',
    'version': '0.1.0',
    'description': 'ToyDL: Deep Learning from Scratch',
    'long_description': '<p align="center" style="font-size:40px; margin:0px 10px 0px 10px">\n    <em>ToyDL</em>\n</p>\n<p align="center">\n    <em>Deep Learning from Scratch</em>\n</p>\n\n\n# Installation\n```bash\npip install toydl\n```\n',
    'author': 'Xiangzhuang Shen',
    'author_email': 'datahonor@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://shenxiangzhuang.github.io/toydl',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
