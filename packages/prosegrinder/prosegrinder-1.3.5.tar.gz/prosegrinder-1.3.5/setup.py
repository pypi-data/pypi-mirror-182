# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['prosegrinder']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'cmudict>=1.0.11,<2.0.0',
 'importlib-metadata>=5.1.0,<6.0.0',
 'narrative>=1.1.1,<2.0.0',
 'pointofview>=1.0.2,<2.0.0',
 'syllables>=1.0.4,<2.0.0']

entry_points = \
{'console_scripts': ['prosegrinder = prosegrinder.__main__:cli']}

setup_kwargs = {
    'name': 'prosegrinder',
    'version': '1.3.5',
    'description': 'A text analytics library for prose fiction.',
    'long_description': '# Prosegrinder\n\n[![Latest PyPI version](https://img.shields.io/pypi/v/prosegrinder.svg)](https://pypi.python.org/pypi/prosegrinder)\n[![GitHub Workflow Status](https://github.com/prosegrinder/python-prosegrinder/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-prosegrinder/actions?query=workflow%3A%22Python+CI%22+branch%3Amain)\n\nA relatively fast, functional prose text counter with readability scoring.\n\n## Installation\n\n`prosegrinder` is available on PyPI. Simply install it with `pip`:\n\n```bash\npip install prosegrinder\n```\n\n## Usage\n\nThe main use is via the `prosegrinder.Prose` object.\n\n```python\n>>> from prosegrinder import Prose\n>>> p = Prose("Some lengthy text that\'s actual prose, like a novel or article.")\n```\n\nThe Prose object will parse everything down and compute basic statistics,\nincluding word count, sentence count, paragraph count, syllable count, point of\nview, dialogue, narrative, and a set of readability scores. All objects and\nattributes should be treated as immutable.\n\nI know this isn\'t great documentation, but it should be enough to get you going.\n\n### Command Line Interface\n\nProsegrinder now includes a simple CLI for analyzing text in a file:\n\n```bash\n$ prosegrinder --help\nUsage: prosegrinder [OPTIONS] FILES...\n\n  Setup the command line interface\n\nOptions:\n  -i, --indent INTEGER  Python pretty-print json indent level.\n  -s, --save FILENAME   File to save output to.\n  --help                Show this message and exit.\n```\n\nWill provide basic statistics on text from a file or set of files including the\nfilename and sh256 of text in each file analyzed. Output is json to help\nfacilitate use in automation::\n\n```json\n[\n  {\n    "filename": "shortstory.txt",\n    "statistics": {\n      "sha256": "5b756dea7c7f0088ff3692e402466af7f4fc493fa357c1ae959fa4493943fc03",\n      "word_character_count": 7008,\n      "phone_count": 5747,\n      "syllable_count": 2287,\n      "word_count": 1528,\n      "sentence_count": 90,\n      "paragraph_count": 77,\n      "complex_word_count": 202,\n      "long_word_count": 275,\n      "pov_word_count": 113,\n      "first_person_word_count": 8,\n      "second_person_word_count": 74,\n      "third_person_word_count": 31,\n      "pov": "first",\n      "readability_scores": {\n        "automated_readability_index": 0.281,\n        "coleman_liau_index": 9.425,\n        "flesch_kincaid_grade_level": 8.693,\n        "flesch_reading_ease": 62.979,\n        "gunning_fog_index": 12.079,\n        "linsear_write": 10.733,\n        "lix": 34.975,\n        "rix": 3.056,\n        "smog": 11.688\n      }\n    }\n  },\n  {\n    "filename": "copyright.txt",\n    "statistics": {\n      "sha256": "553bfd087a2736e4bbe2f312e3d3a5b763fb57caa54e3626da03b0fd3f42e017",\n      "word_character_count": 222,\n      "phone_count": 169,\n      "syllable_count": 78,\n      "word_count": 46,\n      "sentence_count": 7,\n      "paragraph_count": 16,\n      "complex_word_count": 10,\n      "long_word_count": 12,\n      "pov_word_count": 1,\n      "first_person_word_count": 1,\n      "second_person_word_count": 0,\n      "third_person_word_count": 0,\n      "pov": "first",\n      "readability_scores": {\n        "automated_readability_index": 1.404,\n        "coleman_liau_index": 8.073,\n        "flesch_kincaid_grade_level": 6.982,\n        "flesch_reading_ease": 56.713,\n        "gunning_fog_index": 11.324,\n        "linsear_write": 3.714,\n        "lix": 32.658,\n        "rix": 1.714,\n        "smog": 9.957\n      }\n    }\n  }\n]\n```\n\n### Readability scores\n\nThe set of scores automatically calculated:\n\n- Automated Readability Index\n- Coleman Liau Index\n- Flesch Kincaid Grade Level\n- Flesch Reading Ease\n- Gunning Fog Index\n- Linsear Write\n- LIX\n- RIX\n- SMOG\n',
    'author': 'David L. Day',
    'author_email': 'david@davidlday.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
