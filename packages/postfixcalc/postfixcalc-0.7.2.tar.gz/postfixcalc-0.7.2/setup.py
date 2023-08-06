# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['postfixcalc']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.12.0,<23.0.0']

setup_kwargs = {
    'name': 'postfixcalc',
    'version': '0.7.2',
    'description': 'the stupid postfix evaluator',
    'long_description': '# postfixcalc\n\nSimple and stupid infix to postfix converter and evaluator.\n\n# How does it work\nThe algorithm is very simple and straightforward\n\n```python\nfrom postfixcalc.pyeval import evaluate\nfrom postfixcalc.parser import (\n    extract_nums_and_ops,\n    flatten_nodes,\n    infix_to_postfix,\n    make_num,\n    parse,\n    relistexpression,\n)\n\nevaluate(\n    infix_to_postfix(\n        make_num(\n            relistexpression(\n                flatten_nodes(\n                    extract_nums_and_ops(\n                        parse(\'(-1) ^ 2\')\n                    ),\n                ),\n            ),\n        ),\n    ),\n)\n```\n## We should trace from bottom to top:\n   1. parse the expression using `ast.parse` function. This function will parse the expression based on Python grammar and math op precedence.\n   2. extract numbers, and operators outta parsed expression\n   3. the extracted list contains many nested lists and tuples, so we flatten most of them\n   4. we generate a better demonstration outta the flattened list\n   5. we make possible strings to numbers, \'-1\' will be -1 and ...\n   6. we generate the postfix notation outta the numbers and operators\n   7. evaluate the result\n\nBut all this pain is done easily thorough `Calc` type in the library\n```python\nfrom postfixcalc import Calc\n\ncalc = Calc(\'(-1) ^ 2\')\nprint(calc.answer)\n```\n\nThis is easy but `Calc` type provide other _cached_propertied_ which are just the results of the upper functions\n```python\nfrom postfixcalc import Calc\n\nc = Calc("2 * -1")\nprint(c.parsed)\nprint(c.extracted)\nprint(c.flattened)\nprint(c.strparenthesized)\nprint(c.listparenthesized)\nprint(c.numerized)\nprint(c.postfix)\nprint(c.answer)\nprint(c.stranswer)\n\n# <ast.BinOp object at 0x7fcd313ecbe0>\n# [([2], <ast.Mult object at 0x7fcd32002a70>, [(<ast.USub object at 0x7fcd32003010>, [1])])]\n# ([2], <ast.Mult object at 0x7fcd32002a70>, (<ast.USub object at 0x7fcd32003010>, [1]))\n# 2 * (-1)\n# [2, \'*\', \'(\', \'-1\', \')\']\n# [2, \'*\', \'(\', -1, \')\']\n# [2, -1, \'*\']\n# -2\n# -2\n```\n\n# Important notes\n1. For safety reasons, calculations are done with a timeout which is absolutely easy to change:\n```python\nc = Calc(\'...\', timeout=10)\n```\ntimeout is in seconds.\n\n2. `answer` property returns the actual object of the answer, whether it is `int` or `float`, BUT if you want to `print` the answer, you should consider the `obj to str conversion` time, it may be quite long or short depending on that obj; because of this `Calc` implements a new propery called `stranswer` which calculates the str repr with a timeout and raises exceptions if it would take long\nAlways use `stranswer` if you want the str repr of the `answer`\n',
    'author': 'Mahdi Haghverdi',
    'author_email': 'mahdihaghverdiliewpl@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
