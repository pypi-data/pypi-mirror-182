# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_mermaid']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-mermaid',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Python-Mermaid\nThis modules aims to implement a simple way for developers/admin-sys/devops to create on-the-fly [Mermaid diagrams](https://mermaid.js.org/).\n\n## Installation\n```shell\npip install python_mermaid\n```\n\n## Getting started\n```py\n# Creating a simple flowchart diagram\nfrom python_mermaid import FlowChart\n\nthe_march_family = [\n    ("Meg","M"),\n    ("Jo", "J"),\n    ("Beth"."B"),\n    ("Amy", "A"),\n    ("Robert March","RM")\n]\n\nlinks = [\n    ("Robert March", "Meg"),\n    ("Robert March", "Jo"),\n    ("Robert March", "Beth"),\n    ("Robert March", "Amy"),\n]\n\nchart = Flowchart(\n    title="Little Women",\n    nodes=the_march_family,\n    links=links\n)\n\nprint(chart)\n```\nReturns the following\n```txt\n---\ntitle: "Little Women"\n---\ngraph LR\nM["Meg"]\nJ["Jo"]\nB["Beth"]\nA["Amy"]\nRM["Robert"]\n\nRM --> M\nRM --> J\nRM --> B\nRM --> A\n```\nwhich results can be seen [here](https://mermaid.live/edit#pako:eNo9jr0KgzAQgF8l3GxewKGgdBJd7FBor0OqV5U2iaTnIOK79xKo2_fdD3wbdL4nyEFrjY4n_lCuEOqJhdTVW3II6NJ2CGYeVd2ia-4IDQ0ID3SVcOUTloIl8ZikECnsmriND61_UuDkcaK0PqnmoOqg8qACMrAUrJl6KdzQKUnjkSwhxMrehHes2-XOLOwvq-sg57BQBsvcG6bzZKTaQv4yn69MZ-Nu3v99_wEheFGF)\n\n\n## Roadmap\n- [ ] **flowchart** setup\n- [ ] Add *styles* for nodes or links\n- [ ] More diagrams !\n\n## Contribute\nWanna help ? Find a bug ?\n1. Do not hesitate to fork the repository and send PRs with your changes\n2. No time to code ? Send a bug/feature issue [here](https://github.com/Dynnammo/python_mermaid/issues/new/choose)',
    'author': 'THIVEND',
    'author_email': 'baptiste.thivend@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
