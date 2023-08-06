# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli',
 'cli.commands',
 'cli.commands.auth',
 'cli.commands.config_promotion',
 'cli.commands.empower_api',
 'cli.commands.empower_discovery',
 'cli.commands.source_types',
 'cli.commands.user_service',
 'cli.common',
 'cli.common.auth']

package_data = \
{'': ['*'], 'cli.common.auth': ['templates/*']}

install_requires = \
['PyJWT>=2.6.0,<3.0.0',
 'PyYAML>=6.0,<7.0',
 'pickleDB>=0.9.2,<0.10.0',
 'pydantic>=1.9.1,<2.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'python-keycloak>=2.0.0,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'typer>=0.5.0,<0.6.0']

entry_points = \
{'console_scripts': ['empowercli = cli.main:app']}

setup_kwargs = {
    'name': 'empower-cli',
    'version': '1.8.1',
    'description': 'Empower cli client for API interaction',
    'long_description': '# Empower cli client\n\nA Command Line Interface ("CLI") is designed to provide rapid access to key Empower functions without the need to construct REST calls manually.\nThe Empower CLI can be used to manage all Empower functions,\nand certain functions may only be available via the CLI.\n\n[Documentation](https://docs.empoweranalytics.io/empower/docs)\n\n## How to start\n\n1. Setup discovery URL `empowercli context set --discovery-url https://discovery.empoweranalytics.io`.\nFollow step 2 or step 3.\n2. Login with your domain if browser flow is used `empowercli auth login <domain>`\n3. Login with credentials flow. To do that export EMPOWER_CLI_CLIENT_ID and EMPOWER_CLI_CLIENT_SECRET into environment variables. Those variables represent keycloak client id and secret. After that type\n`empowercli auth login-pipeline`\n4. After the login, cli lists information for this domain from the discovery service. Now you can copy one of the available empower api URLs and setup it up for context.\n`empowercli empowercli context set --api-url <api-url>`\n5. Now cli is able to perform commands to api endpoints, for example `empowercli api sources list`\nAll other commands could be checked in [docs](https://docs.empoweranalytics.io/empower/docs/cli) or with empowercli --help\n',
    'author': 'Empower Team',
    'author_email': 'empower@hitachisolutions.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hitachisolutionsamerica/empower/tree/development/tools/empower_cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
