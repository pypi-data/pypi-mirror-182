# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['cawspr']
install_requires = \
['typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['cawspr = cawspr:cli_main']}

setup_kwargs = {
    'name': 'cawspr',
    'version': '0.1.0',
    'description': 'Case and word separation preserving replace',
    'long_description': "# cawspr\n\nCase And Word Separation Preserving Replace (CAWSPR)\n\n## What does this do?\n\nThis script is as simple as it is stupid: You give it a list of words to\nreplace (e.g. `hello world`) and a list of words to replace them with (e.g.\n`goodbye world`) and it will perform this replacement for various compositions\nof these words that are common e.g. in programming:\n\n- separated by spaces: `hello world` → `goodbye world`\n- lowercase and separated by underscores (snake_case):\n  `hello_world` → `goodbye_world`\n- uppercase and separated by underscores (SCREAMING_SNAKE_CASE):\n  `HELLO_WORLD` → `GOODBYE_WORLD`\n- lowercase and separated by hyphens (kebab-case):\n  `hello-world` → `goodbye-world`\n- separated only by capitalizing the first letter of each word (CamelCase):\n  `HelloWorld` → `GoodbyeWorld`\n- separated only by capitalizing the first letter of each word except the first\n  (lowerCamelCase):\n  `helloWorld` → `goodbyeWorld`\n\nThe text in which to make these replacements must be piped into the script's\nstandard input and it will output the resulting modified text to standard\noutput.\n\nThat's it.\n\n## Installation\n\n```bash\npip3 install git+https://gitlab.com/smheidrich/cawspr.git\n```\n\n## Usage\n\nReplacing all occurrences of `hello world` and its variants in a file\n`original.txt` with `goodbye world` and writing the result to `replaced.txt`:\n\n```bash\ncat original.txt | cawspr 'hello world' 'goodbye world' > replaced.txt\n```\n\n## Advertisement\n\nWant to perform such replacements for both file contents *and* file paths in a\ndirectory recursively? Consider\n[full-apply](https://gitlab.com/smheidrich/full-apply) which works great with\ncawspr!\n\n## Similar projects and other resources\n\n- [Softwarerecs StackExchange\n  question](https://softwarerecs.stackexchange.com/q/84786/13721) in which I\n  asked if anyone knows of an existing CLI tool that does this (perhaps more\n  will crop up in the future)\n- The answers to [this StackOverflow question] are full of links to vim plugins\n  for the same purpose (but I wanted it as a CLI tool):\n  - [abolish.vim](https://github.com/tpope/vim-abolish) (can do this and other\n    loosely related things)\n  - [SmartCase](https://www.vim.org/scripts/script.php?script_id=1359)\n  - [keepcase.vim](https://www.vim.org/scripts/script.php?script_id=6)\n",
    'author': 'smheidrich',
    'author_email': 'smheidrich@weltenfunktion.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
