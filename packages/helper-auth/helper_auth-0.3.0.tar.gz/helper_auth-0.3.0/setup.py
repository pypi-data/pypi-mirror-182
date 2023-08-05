# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['helper_auth']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2,<3']

setup_kwargs = {
    'name': 'helper-auth',
    'version': '0.3.0',
    'description': 'Requests authentication using existing helpers',
    'long_description': '[![helper-auth on PyPI](https://img.shields.io/pypi/v/helper-auth)][PyPI]\n\n\n# Installation\n\n```\npip install helper-auth\n```\n\n\n# Usage\n\nObjects of the `HelperAuth` class are intended to be used as custom\nauthentication handlers as per the\n[Requests documentation](https://requests.readthedocs.io/en/latest/user/authentication/#new-forms-of-authentication).\n\n\n## Default scenario\n\nSuppose you have an existing GitHub personal access token, and a\n[Git credential helper](https://git-scm.com/docs/gitcredentials#_custom_helpers)\nalready set up for Git to authenticate to GitHub using this token as\nthe password. This helper prints the following to standard output:\n\n```\n$ git credential-github\nusername=your_github_username\npassword=your_github_token\n```\n\nYou want to use the same token to make GitHub API calls in Python with\nthe help of the Requests library. The API expects a\n`token your_github_token` string as the value of\nyour request\'s `Authorization` header.\n\nYou can use a `HelperAuth` authentication handler with its default settings:\n\n```python\nimport requests\nfrom helper_auth import HelperAuth\n\nauth = HelperAuth("git credential-github")\n\nresponse = requests.get("https://api.github.com/user/repos", auth=auth)\n```\n\n\n## Specifying the helper command\n\nSimple helper command with no command-line arguments can be a string or\na path-like object.\n\n```python\nauth = HelperAuth("helper")\n```\n\n```python\nauth = HelperAuth(Path("helper"))\n```\n\nIf the helper command contains command-line arguments, it can be a string or\na list of strings.\n\n```python\nauth = HelperAuth("helper --option arg")\n```\n\n```python\nauth = HelperAuth(["helper", "--option", "arg"])\n```\n\n\n## Caching the token\n\nBy default, a `HelperAuth` authentication handler never stores the value of\nthe token (password) in its internal state. Rather, the helper command is\ninvoked on each call to the handler. This is an intentional precaution\n(such that the token cannot be retrieved *ex post* by the introspection\nof the handler) but can be expensive. You can override this by\npassing `cache_token=True` to the constructor:\n\n```python\nauth = HelperAuth("helper", cache_token=True)\n```\n\n[PyPI]: https://pypi.org/project/helper-auth\n',
    'author': 'Michal Porteš',
    'author_email': 'michalportes1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mportesdev/helper-auth',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
