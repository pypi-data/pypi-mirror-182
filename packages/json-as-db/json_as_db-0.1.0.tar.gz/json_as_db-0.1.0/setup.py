# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['json_as_db']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=22.1.0']

setup_kwargs = {
    'name': 'json-as-db',
    'version': '0.1.0',
    'description': 'Using JSON as very lightweight database',
    'long_description': '# JSON-as-DB\n\n![Python Version Badge] [![PyTest Badge]](https://github.com/joonas-yoon/json-as-db/actions/workflows/pytest.yml) ![Wheel Badge] [![Hits Badge]](#)\n\nUsing JSON as very lightweight database\n\n## Installation\n\nInstalling via pip:\n\n```bash\npip install json-as-db\n```\n\nInstalling via GitHub repository,\n\n```bash\ngit clone https://github.com/joonas-yoon/json-as-db.git\npip install -e json-as-db\n```\n\n## Contributing\n\nContributing guidelines can be found [CONTRIBUTING.md](CONTRIBUTING).\n\nWelcome all contributions to the community and feel free to contribute.\n\n## License\n\nUnder the MIT license. See the [LICENSE] file for more info.\n\n\n[Python Version Badge]: https://img.shields.io/pypi/pyversions/json-as-db?style=flat-square\n[PyTest Badge]: https://github.com/joonas-yoon/json-as-db/actions/workflows/pytest.yml/badge.svg\n[Wheel Badge]: https://img.shields.io/pypi/wheel/json-as-db?style=flat-square\n[Hits Badge]: https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjoonas-yoon%2Fjson-as-db\n[CONTRIBUTING]: CONTRIBUTING.md\n[LICENSE]: LICENSE\n',
    'author': 'Joonas',
    'author_email': 'joonas.yoon@gmail.com',
    'maintainer': 'Joonas',
    'maintainer_email': 'joonas.yoon@gmail.com',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
