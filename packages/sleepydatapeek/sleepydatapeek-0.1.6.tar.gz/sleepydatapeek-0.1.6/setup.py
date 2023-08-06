# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sleepydatapeek', 'option_utils', 'df_utils']
install_requires = \
['pandas>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'sleepydatapeek',
    'version': '0.1.6',
    'description': 'Peek at local datafiles fast!',
    'long_description': '# **DataPeek**\n*A quick way to peek at local datafiles.*\n\n<br />\n\n## **Welcome to sleepydatapeek!**\nIn short, it\'s hand to have something be able to spit out a configurable preview of data from a file, and bonus points if you can just as easily output in markdown. It would also be nice if said tool could read all the formats.\\\n**DataPeek** has entered the chat!\n\n<br />\n\n### **Table of Contents** 📖\n<hr>\n\n  - **Get Started**\n  - Usage\n  - Technologies\n  - Contribute\n  - Acknowledgements\n  - License/Stats/Author\n\n<br />\n\n## **Get Started 🚀**\n<hr>\n\nThis repo is currently private, so adding this package is all the user needs to care about.\n\n<br />\n\n## **Usage ⚙**\n<hr>\n\nAfter setting up the tool, run `./sleepydatapeek.py [-h|--help]` to display this message:\n```txt\nThis tool takes an input file path and outputs a limited dataframe to either stdout or a markdown file.\n\n\nLimit defaults to 20 rows, and can be overwritten.\nFormat value has synonyms \'xlsx\' and \'xls\'\n--------------\nUsage:\n  ./sleepydatapeek.py --format=[parquet|csv|json|excel] --path=<path> [--output=<path>] [--limit=<row-limit>]\nExamples:\n  ./sleepydatapeek.py --format=csv --path=sample-data/data.csv\n  ./sleepydatapeek.py --format=csv --path=sample-data/data.csv --limit=6\n  ./sleepydatapeek.py --format=csv --path=sample-data/data.csv --output=results.md\nInfo:\n  ./sleepydatapeek.py [-h|--help]\n--------------\n```\n\n<br />\n\n## **Technologies 🧰**\n<hr>\n\n  - [Pandas](https://pandas.pydata.org/docs/)\n\n<br />\n\n## **Contribute 🤝**\n<hr>\n\nAs stated in the welcome section, the corresponding GitHub repo is private. \\\nHowever, feel free to [reach out with opinions](https://github.com/anthonybench)!\n\n<br />\n\n## **Acknowledgements 💙**\n<hr>\n\nCheers to the chaos of modern life for needing personalized agility in schema assessment.\n\n<br />\n\n## **License, Stats, Author 📜**\n<hr>\n\n<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />\n\n<!-- badge cluster -->\n\n![PyPI - License](https://img.shields.io/pypi/l/sleepydatapeek?style=plastic)\n\n<!-- / -->\nSee [License](TODO) for the full license text.\n\nThis package was authored by *Isaac Yep*.',
    'author': 'anthonybench',
    'author_email': 'anythonybenchyep@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anthonybench/datapeek',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
