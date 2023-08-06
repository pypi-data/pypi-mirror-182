# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['trinary']
setup_kwargs = {
    'name': 'trinary',
    'version': '0.1.0',
    'description': '',
    'long_description': '![License](https://img.shields.io/github/license/travisjungroth/trinary?color=blue)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n# trinary - A Python implementation of three-valued logic\ntrinary is a Python library for working with three-valued logic. It allows you to represent and manipulate statements with three possible truth values: true, false, and unknown. Unknown represents the possibility of true and false.\n\n# Usage\nTo use trinary, import `Unknown` into your Python project. You can then use `Unknown` alongside `True` and `False`.\n```python\nfrom trinary import Unknown\n\nx = Unknown\ny = True\nz = False\n```\n\ntrinary works with the standard comparisons and bitwise operators.\n```python\nfrom trinary import Unknown\n\n# Logical AND\nprint(Unknown & True)      # Unknown\nprint(Unknown & False)     # False\nprint(Unknown & Unknown)   # Unknown\n\n# Logical OR\nprint(Unknown | True)      # True\nprint(Unknown | False)     # Unknown\nprint(Unknown | Unknown)   # Unknown\n\n# Logical XOR\nprint(Unknown ^ True)      # Unknown\nprint(Unknown ^ False)     # Unknown\nprint(Unknown | Unknown)   # Unknown\n\n# Logical NOT\nprint(~Unknown)            # Unknown\n\n# Comparisons\nprint(Unknown == True)     # Unknown\nprint(Unknown == False)    # Unknown\nprint(Unknown == Unknown)  # Unknown   \nprint(Unknown != True)     # Unknown\nprint(Unknown != False)    # Unknown\nprint(Unknown != Unknown)  # Unknown\nprint(Unknown < True)      # Unknown\nprint(Unknown < False)     # False\nprint(Unknown < Unknown)   # Unknown   \nprint(Unknown <= True)     # True\nprint(Unknown <= False)    # Unknown\nprint(Unknown <= Unknown)  # Unknown   \nprint(Unknown > True)      # False\nprint(Unknown > False)     # Unknown\nprint(Unknown > Unknown)   # Unknown   \nprint(Unknown >= True)     # Unknown\nprint(Unknown >= False)    # True\nprint(Unknown >= Unknown)  # Unknown\n```\nTo cast to a `bool`, use strictly or weakly to decide how `Unknown` is cast.\n\n```python\nfrom trinary import Unknown, strictly, weakly\n\ncorrect = Unknown\nprint(strictly(correct))  # False\nprint(weakly(correct))    # True\nprint(weakly(True))       # True\nprint(weakly(False))      # True\nprint(weakly(\'\'))         # False\nprint(weakly(\' \'))        # True\n```\n\nUse trinary to represent the truth value of a statement with uncertain information.\n\n```python\nfrom trinary import Trinary, Unknown, strictly, weakly\n\n\ndef hot_out(weather: str) -> Trinary:\n    if weather == "sunny":\n        return True\n    elif weather == "cloudy":\n        return Unknown\n    else:\n        return False\n\n\ndef going_to_the_beach(weather: str, off_work: Trinary) -> Trinary:\n    return hot_out(weather) & off_work\n\n\nmonday_beach = going_to_the_beach(weather="cloudy", off_work=False)\nprint(monday_beach)              # False\nsaturday_beach = going_to_the_beach(weather="cloudy", off_work=True)\nprint(saturday_beach)            # Unknown\ndefinitely_free_saturday = strictly(~saturday_beach)\nprint(definitely_free_saturday)  # False\n```\n# Theory\ntrinary implements Stephen Cole Kleene\'s ["strong logic of indeterminacy"](https://en.wikipedia.org/wiki/Three-valued_logic#Kleene_and_Priest_logics), also called K3. This is equivalent to SQL logic with `NULL`.\n\n### Truth Table\n|p|q|p&q|p^q|p⇒q|¬p|\n|-|-|---|---|---|--|\n|T|T|T  |F  |T  |F |\n|F|F|F  |F  |T  |T |\n|F|?|F  |?  |?  |T |\n|?|T|?  |?  |T  |? |\n|?|F|F  |?  |?  |? |\n|?|?|?  |?  |?  |? |\n\n# License\ntrinary is licensed under the [MIT License](license.md).',
    'author': 'Travis Jungroth',
    'author_email': 'jungroth@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
