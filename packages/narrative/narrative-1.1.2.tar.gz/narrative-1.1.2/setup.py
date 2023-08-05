# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['narrative']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=5.1.0,<6.0.0']

setup_kwargs = {
    'name': 'narrative',
    'version': '1.1.2',
    'description': 'A small Python package for splitting text into dialogue and narrative.',
    'long_description': '# narrative\n\n[![Latest PyPI version](https://img.shields.io/pypi/v/narrative.svg)](https://pypi.python.org/pypi/narrative)\n[![GitHub Workflow Status](https://github.com/prosegrinder/python-narrative/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-narrative/actions?query=workflow%3A%22Python+CI%22+branch%3Amain)\n\nA small Python package for splitting text into dialogue and narrative.\n\n## Installation\n\n`narrative` is available on PyPI. Simply install it with `pip`:\n\n```bash\npip install narrative\n```\n\n## Usage\n\n`narrative` splits a piece of prose into narrative and dialogue components. The\nmain function `split()` will return a dict containing both `narrative` and\n`dialogue` components:\n\n```python\n>>> import narrative\n>>> text = \'"Hello," he said. "How are you today?"\'\n>>> narrative.split(text)\n{\'dialogue\': [\'"Hello,"\', \'"How are you today?"\'], \'narrative\': [\'\', \' he said. \', \'\']}\n```\n\nThere are two other helper functions as well.\n\n`get_dialogue()` returns only the dialogue components:\n\n```python\n>>> narrative.get_dialogue(text)\n[\'"Hello,"\', \'"How are you today?"\']\n```\n\n`get_narrative()` returns only the narrative components:\n\n```python\n>>> narrative.get_narrative(text)\n[\'\', \' he said. \', \'\']\n```\n\nNote: The empty strings are a feature of Python\'s `split()` function. See\n[Why are empty strings returned in split() results?](https://stackoverflow.com/questions/2197451/why-are-empty-strings-returned-in-split-results#2197493)\nfor an explanation.\n\n### British Style\n\nEach function accepts a second parameter of a regular expression used to parse\nout the dialogue. This defaults to `narrative.DIALOGUE_RE`, which follows the\nAmerican standard of using double quotes for initial quotes. `narrative` now\nincludes a second regular expression, `narrative.BRITISH_DIALOGUE_RE`, which\nfollows the British style of using single quotes for initial quotes. Simply use\nit as the second parameter for any function:\n\n```python\n>>> import narrative\n>>> narrative.split(text, narrative.BRITISH_DIALOGUE_RE)\n>>> …\n>>> narrative.get_dialogue(text, narrative.BRITISH_DIALOGUE_RE)\n>>> …\n>>> narrative.get_narrative(text, narrative.BRITISH_DIALOGUE_RE)\n>>> …\n```\n',
    'author': 'David L. Day',
    'author_email': 'david@davidlday.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/prosegrinder/python-narrative',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
