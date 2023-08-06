# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textual_select']

package_data = \
{'': ['*']}

install_requires = \
['textual>=0.6.0']

setup_kwargs = {
    'name': 'textual-select',
    'version': '0.1.1',
    'description': 'A select widget (aka dropdown) for Textual.',
    'long_description': '# Textual: Select\n\nA simple select widget (aka dropdown) for [textual](https://github.com/Textualize/textual).\n\n## Usage\n\n```python\nfrom textual_select import Select\n\ndropdown_data = [\n    {"value": 0, "text": "Pick-Up"},\n    {"value": 1, "text": "SUV"},\n    {"value": 2, "text": "Hatchback"},\n    {"value": 3, "text": "Crossover"},\n    {"value": 4, "text": "Convertible"},\n    {"value": 5, "text": "Sedan"},\n    {"value": 6, "text": "Sports Car"},\n    {"value": 7, "text": "Coupe"},\n    {"value": 8, "text": "Minivan"}\n]\n\nSelect(\n    placeholder="please select",\n    items=dropdown_data,\n    list_mount="#main_container"\n)\n```\n\n## Installation\n\n```bash\npip install textual-select\n```\n\nRequires textual 0.6.0 or later.\n',
    'author': 'Mischa Schindowski',
    'author_email': 'mschindowski@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mitosch/textual-select',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
