# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['general_q', 'general_q.agents', 'general_q.decoders', 'general_q.encoders']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'general-q',
    'version': '0.1.0',
    'description': 'An easy to use library for general purpose reinforcement learning and experimentation',
    'long_description': '# general_q\n\n<div align="center">\n\n[![Build status](https://github.com/khoda81/general_q/workflows/build/badge.svg?branch=master&event=push)](https://github.com/khoda81/general_q/workflows/build/badge.svg?branch=master&event=push)\n[![Python Version](https://img.shields.io/pypi/pyversions/general_q.svg)](https://pypi.org/project/general_q/)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/khoda81/general_q/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/khoda81/general_q/releases)\n[![License](https://img.shields.io/github/license/khoda81/general_q)](https://github.com/khoda81/general_q/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\nAn easy to use library for general purpose reinforcement learning and experimentation\n\n</div>\n\n## Installation\n\n```bash\npip install -U general_q\n```\n\nor install with `Poetry`\n\n```bash\npoetry add general_q\n```\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/khoda81/general_q)](https://github.com/khoda81/general_q/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license.\nSee [LICENSE](https://github.com/khoda81/general_q/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```bibtex\n@misc{general_q,\n  author = {axiom},\n  title = {An easy to use library for general purpose reinforcement learning and experimentation},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/khoda81/general_q}}\n}\n```\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n',
    'author': 'axiom',
    'author_email': '20.mahdikh.0@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/khoda81/general_q',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
