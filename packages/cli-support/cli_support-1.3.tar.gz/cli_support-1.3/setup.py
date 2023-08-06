# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli_support']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cli-support',
    'version': '1.3',
    'description': 'Support component license information (CLI) files',
    'long_description': '# CLI Support for Python\n\nPython library to read Component License Information (CLI) files. They can be\ncreated by [FOSSology](https://www.fossology.org) and stored in\n[SW360](https://www.eclipse.org/sw360/).\n\nFor more information about the CLI file format, please have a look at\n[ComponentLicenseInformation.md](ComponentLicenseInformation.md).\n\n## Usage\n\n### Installation\n\nThis project is available as [Python package on PyPi.org](https://pypi.org/project/cli-support/).  \nInstall cli_support and required dependencies:\n\n  ```shell\n  pip install cli\n  ```\n\n### Required Packages\n\n* none\n\n## Using the API\n\n* Start using the API:\n\n  ```python\n  import cli\n  clifile = cli.CLI.CliFile()\n  clifile.read_from_file("cli_filename")\n  ```\n\n## Contribute\n\n* All contributions in form of bug reports, feature requests or merge requests are welcome!\n* Please use proper [docstrings](https://realpython.com/documenting-python-code/) to document\n  functions and classes.\n* Extend the testsuite **poetry run pytest** with the new functions/classes\n\n## Build\n\n### Building Python package\n\nFor building the library, you need [Poetry](https://python-poetry.org/). Build is then\nsimply triggered using\n\n```shell\npoetry build\n```\n\nThis creates the source and wheel files in ```dist/``` subdirectory -- which can then\nbe uploaded or installed locally using ```pip```.\n\n## Test\n\nStart the complete test suite or a specific test case (and generate coverage report):\n\n```shell\npoetry run pytest\n```\n\nor\n\n```shell\npoetry run coverage run -m pytest\npoetry run coverage report -m --omit "*/site-packages/*.py"\npoetry run coverage html --omit "*/site-packages/*.py"\n```\n\n## Demo\n\nThe script ``show_licenses.py`` shows how to use the library to retrieve some information\nof a given CLI file.\n\n```shell\npython ./show_licenses.py ./test/testfiles/CLIXML_MIT_simple.xml\n```\n\n## License\n\nThe project is licensed under the MIT license.  \nSPDX-License-Identifier: MIT\n',
    'author': 'Thomas Graf',
    'author_email': 'thomas.graf@siemens.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
