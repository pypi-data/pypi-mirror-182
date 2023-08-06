# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['llm_strategy',
 'llm_strategy.testing',
 'llm_strategy.testing.tests',
 'llm_strategy.tests']

package_data = \
{'': ['*']}

install_requires = \
['docstring-parser>=0.15,<0.16',
 'langchain>=0.0.42,<0.0.43',
 'openai>=0.25.0,<0.26.0',
 'parse>=1.19.0,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'llm-strategy',
    'version': '0.0.1.dev0',
    'description': 'Directly Connecting Python to LLMs - Dataclasses & Interfaces <-> LLMs',
    'long_description': '# llm-strategy\n\n[![Release](https://img.shields.io/github/v/release/blackhc/llm-strategy)](https://img.shields.io/github/v/release/blackhc/llm-strategy)\n[![Build status](https://img.shields.io/github/actions/workflow/status/blackhc/llm-strategy/main.yml?branch=main)](https://github.com/blackhc/llm-strategy/actions/workflows/main.yml?query=branch%3Amain)\n[![codecov](https://codecov.io/gh/blackhc/llm-strategy/branch/main/graph/badge.svg)](https://codecov.io/gh/blackhc/llm-strategy)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/blackhc/llm-strategy)](https://img.shields.io/github/commit-activity/m/blackhc/llm-strategy)\n[![License](https://img.shields.io/github/license/blackhc/llm-strategy)](https://img.shields.io/github/license/blackhc/llm-strategy)\n\nImplementing the Strategy Pattern using LLMs.\n\nThis package adds a decorator `llm_strategy` that connects to an LLM (such as OpenAI’s GPT-3) and uses the LLM to implement abstract methods in interface classes. It does this by forwarding requests to the LLM and converting the responses back to Python data using Python\'s ``@dataclasses`.\n\nIt uses the doc strings, type annotations, and method/function names as prompts for the LLM, and can automatically convert the results back into Python types (currently only supporting `@dataclasses`). It can also extract a data schema to send to the LLM for interpretation. While the `llm-strategy` package still relies on some Python code, it has the potential to reduce the need for this code in the future by using additional, cheaper LLMs to automate the parsing of structured data.\n\n- **Github repository**: <https://github.com/blackhc/llm-strategy/>\n- **Documentation** <https://blackhc.github.io/llm-strategy/>\n\n## Example\n\n```python\nfrom dataclasses import dataclass\nfrom llm_strategy import llm_strategy\nfrom langchain.llms import OpenAI\n\n\n@llm_strategy(OpenAI(max_tokens=256))\n@dataclass\nclass Customer:\n    key: str\n    first_name: str\n    last_name: str\n    birthdate: str\n    address: str\n\n    @property\n    def age(self) -> int:\n        """Return the current age of the customer.\n\n        This is a computed property based on `birthdate` and the current year (2022).\n        """\n\n        raise NotImplementedError()\n\n\n@dataclass\nclass CustomerDatabase:\n    customers: list[Customer]\n\n    def find_customer_key(self, query: str) -> list[str]:\n        """Find the keys of the customers that match a natural language query best (sorted by closeness to the match).\n\n        We support semantic queries instead of SQL, so we can search for things like\n        "the customer that was born in 1990".\n\n        Args:\n            query: Natural language query\n\n        Returns:\n            The index of the best matching customer in the database.\n        """\n        raise NotImplementedError()\n\n    def load(self):\n        """Load the customer database from a file."""\n        raise NotImplementedError()\n\n    def store(self):\n        """Store the customer database to a file."""\n        raise NotImplementedError()\n\n\n@llm_strategy(OpenAI(max_tokens=1024))\n@dataclass\nclass MockCustomerDatabase(CustomerDatabase):\n    def load(self):\n        self.customers = self.create_mock_customers(10)\n\n    def store(self):\n        pass\n\n    @staticmethod\n    def create_mock_customers(num_customers: int = 1) -> list[Customer]:\n        """\n        Create mock customers with believable data (our customers are world citizens).\n        """\n        raise NotImplementedError()\n```\n\nSee [examples/customer_database_search.py](examples/customer_database_search.py) for a full example.\n\n![Customer Database Viewer](examples/app.svg)\n\n![Searching for a Customer](examples/search1.svg)\n\n![Searching for a Customer](examples/search2.svg)\n\n## Getting started with contributing\n\nClone the repository first. Then, install the environment and the pre-commit hooks with \n\n```bash\nmake install\n```\n\nThe CI/CD\npipeline will be triggered when you open a pull request, merge to main,\nor when you create a new release.\n\nTo finalize the set-up for publishing to PyPi or Artifactory, see\n[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).\nFor activating the automatic documentation with MkDocs, see\n[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).\nTo enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).\n\n## Releasing a new version\n\n- Create an API Token on [Pypi](https://pypi.org/).\n- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting \n[this page](https://github.com/blackhc/llm-strategy/settings/secrets/actions/new).\n- Create a [new release](https://github.com/blackhc/llm-strategy/releases/new) on Github. \nCreate a new tag in the form ``*.*.*``.\n\nFor more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).\n\n---\n\nRepository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).',
    'author': 'Andreas Kirsch, Daedalus Lab Ltd',
    'author_email': 'blackhc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/blackhc/llm-strategy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
