# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['unitestify']
install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['unitestify = unitestify:unitestify']}

setup_kwargs = {
    'name': 'unitestify',
    'version': '0.1.0',
    'description': 'Base unittest scaffold package',
    'long_description': '# Unitestify - Generate skeleton test file from Python file.\n\nSupport Unnitests and Django tests.\n\n## How to use this package?\n\n\n```bash\npython unitestify --help\nUsage: unitestify.py [OPTIONS]\n\n  Unitestify command line arguments.\n\nOptions:\n  --file TEXT  Path to file from which to generate test file\n  --type TEXT  Type of test to generate\n  --help       Show this message and exit.\n```\n\nThere are two commands available:\n    * `--file` - Requires path to a Python file from which you want to generate the base test file.\n    * `--type` - Test type, `unittest` either `django`\n\n\n## Example\n\n`data.py`\n\n```python\nclass Manager:\n\n    def manage_data(self):\n        return "Managing data"\n\n    def retrieve_data(self):\n        return "Retrieved data"\n```\n\nHere is our output file.\n\n`test_data.py`\n\n```python\nimport unittest\n\nclass TestManager(unittest.TestCase):\n    """TestManager."""\n\n    def test_manage_data(self):\n        """Test manage data."""\n\n    def test_retrieve_data(self):\n        """Test retrieve data."""\n```\n',
    'author': 'Viktor Sokolov',
    'author_email': 'viktorsokolov.and@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/victory-sokolov/unitestify',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
