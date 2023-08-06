# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpt_do',
 'gpt_do.doers',
 'gpt_do.vendor.chatgpt_wrapper',
 'gpt_do.vendor.chatgpt_wrapper.chatgpt_wrapper']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'openai>=0.25.0,<0.26.0',
 'playwright>=1.29.0,<2.0.0',
 'retry>=0.9.2,<0.10.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['do = gpt_do.cli:do']}

setup_kwargs = {
    'name': 'gpt-do',
    'version': '0.1.7',
    'description': 'GPT-powered bash commands.',
    'long_description': '# `gpt-do`\n\nThis is a handy-dandy CLI for when you don\'t know wtf to do.\n\nInstead of furiously grepping through man pages, simply use `do`, and have GPT-3 do all the magic for you.\n\n## Installation\n\nWe recommend using [`pipx`](https://pypa.github.io/pipx/):\n\n```console\n$ pipx install gpt-do\n$ which do\n```\n\nHowever you can also use `pip`:\n\n```console\n$ pip install gpt-do\n$ which do\n```\n\n```\n## Usage\n\n```console\n$ export OPENAI_API_KEY=xxx # stick this in your bash_profile\n$ do amend the message of my last commit to "It works!"\nThis command will amend the message of the last commit to \'It works!\'.\ngit commit --amend -m \'It works!\'\nDo you want to continue? [y/N]: y\n[main 3e6a2f6] It works!!\n Date: Thu Dec 22 01:15:40 2022 -0800\n 5 files changed, 1088 insertions(+)\n create mode 100644 .gitignore\n create mode 100644 .gitmodules\n create mode 100644 README.md\n create mode 100644 poetry.lock\n create mode 100644 pyproject.toml\n```\n',
    'author': 'Yasyf Mohamedali',
    'author_email': 'yasyfm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yasyf/gpt-do',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
