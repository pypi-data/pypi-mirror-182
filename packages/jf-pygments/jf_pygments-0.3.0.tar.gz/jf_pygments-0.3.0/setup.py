# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jf_pygments', 'jf_pygments.lexers', 'jf_pygments.styles']

package_data = \
{'': ['*']}

install_requires = \
['pygments>=2.13.0,<3.0.0']

entry_points = \
{'pygments.lexers': ['baldrsql = jf_pygments:BaldrSqlLexer'],
 'pygments.styles': ['baldr = jf_pygments:BaldrStyle',
                     'white = jf_pygments:WhiteStyle']}

setup_kwargs = {
    'name': 'jf-pygments',
    'version': '0.3.0',
    'description': 'Extend the Python syntax highlighter with some custom lexers and styles.',
    'long_description': 'jf_pygments\n===========\n\nExtend the Python syntax highlighter with some custom lexers and styles.\n\nhttps://pygments.org/docs/plugins/\n\n::\n\n    pip install --user "pygments[plugins]"\n\n::\n\n    pip install --user jf_pygments\n\nhttps://python-poetry.org/docs/pyproject/#plugins\n\n.. code-block:: toml\n\n    [tool.poetry.plugins]\n\n    [tool.poetry.plugins."pygments.styles"]\n    white = "jf_pygments:WhiteStyle"\n    baldr = "jf_pygments:BaldrStyle"\n\n    [tool.poetry.plugins."pygments.lexers"]\n    baldrsql = "jf_pygments:BaldrSqlLexer"\n',
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Josef-Friedrich/jf_pygments',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
