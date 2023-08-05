# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pointofview']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=5.1.0,<6.0.0']

setup_kwargs = {
    'name': 'pointofview',
    'version': '1.0.4',
    'description': "A Python package for determining a piece of text's point of view (first, second, third, or unknown).",
    'long_description': '# pointofview\n\n[![Latest PyPI version](https://img.shields.io/pypi/v/pointofview.svg)](https://pypi.python.org/pypi/pointofview)\n[![GitHub Workflow Status](https://github.com/prosegrinder/python-pointofview/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-pointofview/actions?query=workflow%3A%22Python+CI%22+branch%3Amain)\n\nA Python package for determining a piece of text\'s point of view (first, second,\nthird, or unknown).\n\n## Installation\n\n`pointofview` is available on PyPI. Simply install it with `pip`:\n\n```bash\npip install pointofview\n```\n\nYou can also install it from source:\n\n```bash\n$ git clone https://github.com/prosegrinder/python-pointofview.git\nCloning into \'python-pointofview\'...\n...\n\n$ cd python-pointofview\n$ python setup.py install\n...\n```\n\n## Usage\n\n`pointofview` guesses a text\'s point of view by counting point of view pronouns.\nThe main function `get_text_pov()` will return \'first\', \'second\', \'third\', or\nnull (Python\'s `None` object):\n\n```python\n>>> import pointofview\n>>> text = "I\'m a piece of text written in first person! What are you?"\n>>> pointofview.get_text_pov(text)\n\'first\'\n```\n\nThere are two other helper functions as well.\n\n`get_word_pov()` returns the point of view of a single word:\n\n```python\n>>> pointofview.get_word_pov("I")\n\'first\'\n>>> pointofview.get_word_pov("nope")\nNone\n```\n\n`parse_pov_words()` returns a dict containing all first-, second-, and\nthird-person point-of-view words:\n\n<!-- markdownlint-disable MD013 -->\n\n```python\n>>> text = """\n... When I try to analyze my own cravings, motives, actions and so forth, I surrender to a sort of retrospective imagination which feeds the analytic faculty with boundless alternatives and which causes each visualized route to fork and re-fork without end in the maddeningly complex prospect of my past.\n... """\n>>> pointofview.parse_pov_words(text)\n{\'first\': [\'i\', \'i\'], \'second\': [], \'third\': []}\n```\n\n<!-- markdownlint-enable MD013 -->\n',
    'author': 'David L. Day',
    'author_email': 'david@davidlday.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/prosegrinder/pointofview',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
