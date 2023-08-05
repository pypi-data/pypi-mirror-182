# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raclients', 'raclients.graph', 'raclients.modelclient']

package_data = \
{'': ['*']}

install_requires = \
['Authlib>=1.2.0,<2.0.0',
 'fastapi>=0.88.0,<0.89.0',
 'gql>=3.4.0,<4.0.0',
 'httpx>=0.23.1,<0.24.0',
 'more-itertools>=9.0.0,<10.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'ramodels==15.4.0',
 'structlog>=22.3.0,<23.0.0',
 'tenacity>=8.1.0,<9.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'raclients',
    'version': '3.0.2',
    'description': 'Clients for OS2mo/LoRa',
    'long_description': '<!--\nSPDX-FileCopyrightText: 2021 Magenta ApS <https://magenta.dk>\nSPDX-License-Identifier: MPL-2.0\n-->\n\n\n# RA Clients\n\nOS2mo/LoRa clients\n\n<!--\n## Versioning\nThis project uses [Semantic Versioning](https://semver.org/) with the following strategy:\n- MAJOR: Incompatible changes to existing data models\n- MINOR: Backwards compatible updates to existing data models OR new models added\n- PATCH: Backwards compatible bug fixes\n\n## Getting Started\n\nTODO: README section missing!\n\n### Prerequisites\n\n\nTODO: README section missing!\n\n### Installing\n\nTODO: README section missing!\n\n## Running the tests\n\nTODO: README section missing!\n\n## Deployment\n\nTODO: README section missing!\n\n## Built With\n\nTODO: README section missing!\n\n## Authors\n\nMagenta ApS <https://magenta.dk>\n\nTODO: README section missing!\n-->\n## License\n- This project: [MPL-2.0](MPL-2.0.txt)\n- Dependencies:\n  - pydantic: [MIT](MIT.txt)\n\nThis project uses [REUSE](https://reuse.software) for licensing. All licenses can be found in the [LICENSES folder](LICENSES/) of the project.\n',
    'author': 'Magenta',
    'author_email': 'info@magenta.dk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://magenta.dk/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
