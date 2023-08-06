# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['codecrumbs']

package_data = \
{'': ['*']}

extras_require = \
{':python_version >= "3.11"': ['executing>=1.2.0,<2.0.0',
                               'asttokens>=2.2.1,<3.0.0']}

entry_points = \
{'console_scripts': ['codecrumbs = codecrumbs.__main__:main'],
 'pytest11': ['codecrumbs = codecrumbs.pytest_plugin']}

setup_kwargs = {
    'name': 'codecrumbs',
    'version': '0.1.0',
    'description': 'leave codecrumbs behind so that other can adopt the changes',
    'long_description': '[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# codecrumbs\n\nCodecrumbs is a Python library (and pytest plugin) for source code refactoring across library boundaries.\nIt allows you to change the API of your library and to propagate this changes to every one who uses your library.\n\n\nMore can be found in the [documentation](https://15r10nk.github.io/codecrumbs/introduction/).\n\n## Example\n\nSimple example which renames one argument:\n\n``` python\nclass Example:\n    # old code ...\n    # def method(self,v):\n    #    print(v)\n\n    @renamed_argument("v", "value")\n    def method(self, value):\n        print(value)\n\n\n# some where else\ne = Example()\n\ne.method(v=5)\n```\n\nand apply the refactoring later\n\n``` bash\n# if you have a standalone script\ncodecrumbs example.py\n# or if you have tests\npytest --codecrumbs-fix test_example.py\n```\n\nwhich will rename the argument\n\n```python\ne.method(value=5)\n```\n\nYou can use `codecrumbs` instead of `python` to execute your code, or `pytest` to run your tests and apply the renamings automatically.\n\nThis can be used to fix the small things in your library you wanted to fix but never did,\nbecause you wanted to stay backwards compatible or didn\'t wanted you user to fix 1000 renamings in their code.\n\n## Installation\n\nYou can install `codecrumbs` via `pip` from [PyPI](https://pypi.org/project):\n\n`pip install codecrumbs`\n\nThe pytest support comes out of the box and everyone who depends on your library can use `pytest --codecrumbs-fix` to apply the changes you declared.\n\n## Features\n\nWith codecrumbs you can fix:\n * method / attribute names\n * rename named arguments of functions\n\n\n## Contributing\nContributions are very welcome. Tests can be run with [tox](https://tox.readthedocs.io/en/latest/), please ensure\nthe coverage at least stays the same before you submit a pull request.\n\n## Issues\n\nIf you encounter any problems, please [file an issue](https://github.com/15r10nk/pytest-codecrumbs/issues) along with a detailed description.\n\n## License\n\nDistributed under the terms of the [MIT](http://opensource.org/licenses/MIT) license, "pytest-codecrumbs" is free and open source software\n',
    'author': 'Frank Hoffmann',
    'author_email': '15r10nk@polarbit.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/15r10nk/codecrumbs',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
