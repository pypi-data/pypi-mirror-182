# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_mermaid']

package_data = \
{'': ['*']}

install_requires = \
['Unidecode>=1.3.6,<2.0.0']

entry_points = \
{'console_scripts': ['test = metabase_query_checker.collection_graph:start']}

setup_kwargs = {
    'name': 'python-mermaid',
    'version': '0.1.3',
    'description': 'A (quite) simple that helps creating on-the-fly Mermaid diagrams',
    'long_description': '# Python-Mermaid\nThis modules aims to implement a simple way for developers/admin-sys/devops to create on-the-fly [Mermaid diagrams](https://mermaid.js.org/).\n\n## Installation\n```shell\npip install python_mermaid\n```\n\n## How to use\nAll examples are available [here](./examples)\n\nRun the script below to see diagram generation\n```py\n# Creating a simple flowchart diagram\nfrom python_mermaid.diagram import (\n    MermaidDiagram,\n    Node,\n    Link\n)\n\n# Family members\nmeg = Node("Meg")\njo = Node("Jo")\nbeth = Node("Beth")\namy = Node("Amy")\nrobert = Node("Robert March")\n\nthe_march_family = [meg, jo, beth, amy, robert]\n\n# Create links\nfamily_links = [\n    Link(robert, meg),\n    Link(robert, jo),\n    Link(robert, beth),\n    Link(robert, amy),\n]\n\nchart = MermaidDiagram(\n    title="Little Women",\n    nodes=the_march_family,\n    links=family_links\n)\n\nprint(chart)\n```\n\nReturns the following\n```txt\n---\ntitle: Little Women\n---\ngraph \nmeg["Meg"]\njo["Jo"]\nbeth["Beth"]\namy["Amy"]\nrobert_march["Robert March"]\nrobert_march ---> meg\nrobert_march ---> jo\nrobert_march ---> beth\nrobert_march ---> amy\n```\nwhich results can be seen [here](https://mermaid.live/edit#pako:eNptj8FOw0AMRH9l5XPzA3tAAnFC9AIHpOIKuYlJUmo72jqHqOq_46zEiZzGbzzS2DdorWPI0DQNqo9-4ZxeRw9NHyasqHXTF5qGhCrcfyLsuUc4op4t4MXqfGIfgp5CKpMsgY-yVCp24uJfQqVdU28V037Ff_sUjQ8pmrbss225a_mWH0fADoSL0NjFlzfUlBB8YGGEHGNH5QcB9R45mt3eF20he5l5B_PUkfPzSPG9QP6myzXcifRg9sf3X1ADb2E)\n\n## Roadmap\nCheck [issues](https://github.com/Dynnammo/python_mermaid/issues) for more information\n\n## Development\n- Requirements: install [Poetry](https://python-poetry.org). Here is the official method below. ⚠️ Please consider getting a look at Poetry\'s documentation if it doesn\'t work. ⚠️\n```shell\ncurl -sSL https://install.python-poetry.org | python3 -\n```\n- All-in-one command below to clone and install dependencies\n```shell\ncurl -sSL https://install.python-poetry.org | python3 -\ngit clone https://github.com/Dynnammo/python_mermaid\ncd python_mermaid\npoetry shell\npoetry install --with dev\n```\n\nTo launch tests:\n```shell\npoetry run pytest\n```\n\nTo check linting:\n```shell\npoetry run flake8\n```\n\nThis project comes with a tool called `pre-commit` that checks if your code is correctly linted.\nIf you want to use it, run the following\n```shell\npre-commit install\n```\n\n## Contribute\nWanna help ? Find a bug ?\n1. Do not hesitate to fork the repository and send PRs with your changes\n2. No time to code ? Send a bug/feature issue [here](https://github.com/Dynnammo/python_mermaid/issues/new/choose)',
    'author': 'Dynnammo',
    'author_email': 'contact@dynnammo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
