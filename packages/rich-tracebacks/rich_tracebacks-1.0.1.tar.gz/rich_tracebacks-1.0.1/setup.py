# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rich_tracebacks']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'rich-tracebacks',
    'version': '1.0.1',
    'description': "Automatic installation of Rich's traceback handler",
    'long_description': '# rich-tracebacks\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rich-tracebacks?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/rich-tracebacks)\n[![PyPI](https://img.shields.io/pypi/v/rich-tracebacks?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/rich-tracebacks)\n[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/rich-tracebacks?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/rich-tracebacks/releases)\n[![PyPI - License](https://img.shields.io/pypi/l/rich-tracebacks?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/rich-tracebacks/blob/main/LICENSE)\n\nrich-tracebacks automates the installation\nof [Rich\'s traceback handler](https://rich.readthedocs.io/en/stable/traceback.html#traceback-handler) in Python\nprograms. Compared to Rich\'s\nown [sanctioned method](https://rich.readthedocs.io/en/stable/traceback.html#automatic-traceback-handler)\nof automatically installing its traceback handler, rich-tracebacks is markedly simpler and agnostic to your virtual\nenvironment.\n\n## Installation\n\n```bash\npip install rich-tracebacks\n```\n\n## Usage\n\n### Enabling\n\nSet the `RICH_TRACEBACKS` environment variable. The value of the variable doesn\'t matter, but we\'ll use `1` as an\nexample.\n\n```bash\nexport RICH_TRACEBACKS=1\n```\n\nThat\'s it. Rich\'s traceback handler will be automatically installed each time you run your program.\n\n### Disabling\n\nUnset the `RICH_TRACEBACKS` environment variable.\n\n```bash\nunset RICH_TRACEBACKS\n```\n\n### Configuration\n\nYou can configure the traceback handler with\nits [supported options](https://rich.readthedocs.io/en/stable/reference/traceback.html#rich.traceback.install)\nby creating an `rt_config.py` file at your project\'s root. The file should contain a dictionary named `config`\nthat maps option names to their intended values. For example:\n\n```python\n# rt_config.py\n\nconfig = {\n    "show_locals": True,\n    "width": 120,\n    "theme": "monokai",\n    ...\n}\n```\n\nOf special note is the `console` option, which takes\na [Rich Console](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.Console) object. To use this\noption, you must import the `Console` class in your `rt_config.py` file. For example:\n\n```python\n# rt_config.py\n\nfrom rich.console import Console\n\nconfig = {\n    "console": Console(file=open("traceback.log", "w")),\n    ...\n}\n```\n\nOptions that are not defined in `rt_config.py` will fall back to their default values. If `rt_config.py`\ndoes not exist, all options will fall back to their default values.\n\n## License\n\nrich-tracebacks is licensed under the [MIT License](https://github.com/celsiusnarhwal/rich-tracebacks/blob/main/LICENSE.md).\n\n\n',
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/celsiusnarhwal/rich-tracebacks',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.3,<4.0.0',
}


setup(**setup_kwargs)
