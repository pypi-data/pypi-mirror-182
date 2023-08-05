# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fizzbuzz']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=6.0.0,<7.0.0', 'setuptools==57.2.0']

setup_kwargs = {
    'name': 'fizzbuzz-a-a-r-2',
    'version': '0.1.0',
    'description': 'Setting up CI project',
    'long_description': '# ExamFinalScripting\n## Who made this project ?\n### Group : \n    - Augustin Marie\n    - Aya Najare\n    - Remi Staelen\n\n## Want to use this project ?\n1. Fork / Clone\n2. Create and activate a virtual environment **without poetry** \n#### Install venv \n```sh\n$ py -m pip install --user virtualenv\n```\n#### Creating virtual env \n```sh\n$ py -m venv env\n```\n#### Activating virtual env\n```sh\n$ .\\env\\Scripts\\activate\n```\n3. Install requirements \n```sh\n$  pip install -r requirements.txt\n```\n4. Install poetry \n```sh\n$  pipx install poetry\n```\n5. Install poetry dependencies \n```sh\n$  poetry install \n```\n6. Activate virtual env **using poetry** \n```sh\n$  poetry shell \n```\n\n\n## Run the tests with poetry:\n### Unit tests\nUnit tests are made with the unittest, to launch them manually, run : \n```sh\n$ poetry run python -m unittest discover\n```\n\n### Functional tests\nFunctional tests are made with behave, to launch them manually, run : \n```sh\n$ poetry run behave\n```\n\n## CI made with\nTo manually run linters with poetry, you can use the following commands : \n### flake8\n```sh\n$ poetry run flake8 .\n```\n### Isort \n```sh\n$ poetry run isort .\n```\n### Bandit \n```sh\n$ poetry run bandit -r .\n```\n## Build & Publish with poetry\n### Authentication \n```sh\n$ poetry config http-basic.pypi <username> <password>\n```\n### Build & Publish \n```sh\n$ poetry publish --build\n```\n\n',
    'author': 'augustin-marie',
    'author_email': 'a.marie189@laposte.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.9',
}


setup(**setup_kwargs)
