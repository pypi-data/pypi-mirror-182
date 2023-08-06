# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sfctools',
 'sfctools.automation',
 'sfctools.bottomup',
 'sfctools.core',
 'sfctools.datastructs',
 'sfctools.gui',
 'sfctools.gui.attune',
 'sfctools.gui.attune.src',
 'sfctools.misc']

package_data = \
{'': ['*'],
 'sfctools.gui': ['attune/src/styles/bright/*', 'attune/src/styles/dark/*']}

install_requires = \
['cattrs==1.0.0',
 'graphviz>=0.19,<0.20',
 'matplotlib>=3.6,<4.0',
 'networkx>2.2',
 'numpy>1.20.1',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>1.3',
 'poetry>=1.1.6,<2.0.0',
 'pydot>=1.4,<2.0',
 'pyperclip>=1.8,<2.0',
 'pyqt5>5.15',
 'pyyaml>=6.0,<7.0',
 'scipy>=1.7.2,<1.9.1',
 'seaborn>=0.11.2,<0.12.0',
 'setuptools>60.0.0',
 'sympy>=1.10']

setup_kwargs = {
    'name': 'sfctools',
    'version': '1.0.3',
    'description': 'Framework for stock-flow consistent agent-based modeling, being developed at the German Aerospace Center (DLR) for and in the scientific context of energy systems analysis, however, it is widely applicable in other scientific fields.',
    'long_description': '# sfctools - A toolbox for stock-flow consistent, agent-based models\n\nSfctools is a lightweight and easy-to-use Python framework for agent-based macroeconomic, stock-flow consistent (ABM-SFC) modeling. It concentrates on agents in economics and helps you to construct agents, helps you to manage and document your model parameters, assures stock-flow consistency, and facilitates basic economic data structures (such as the balance sheet).\n\n\n## Installation\n\nWe recommend to install sfctools in a fresh Python 3.8 environment. Then, in a terminal of your choice, type:\n\n    pip install sfctools\n\nsee https://pypi.org/project/sfctools/\n\n## Usage with Graphical User Interface \'Attune\'\n\nType\n\n    python -m sfctools attune\n\nto start the GUI.\n\n## Usage inside Python\n\n```console\nfrom sfctools import Agent,World\nclass MyAgent(Agent):\n    def __init__(self, a):\n        super().__init__(self)\n        self.some_attribute = a\nmy_agent = MyAgent()\nprint(my_agent)\nprint(World().get_agents_of_type("MyAgent"))\n```\n\n\n| Author Thomas Baldauf, German Aerospace Center (DLR), Curiestr. 4 70563 Stuttgart | thomas.baldauf@dlr.de |\n',
    'author': 'Thomas Baldauf',
    'author_email': 'thomas.baldauf@dlr.de',
    'maintainer': 'Thomas Baldauf, Benjamin Fuchs',
    'maintainer_email': 'thomas.baldauf@dlr.de, benjamin.fuchs@dlr.de',
    'url': 'https://gitlab.com/dlr-ve/esy/sfctools/framework',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
