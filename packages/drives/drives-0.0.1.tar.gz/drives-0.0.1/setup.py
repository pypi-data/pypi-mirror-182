# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drives']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'drives',
    'version': '0.0.1',
    'description': 'Drives for Humans™',
    'long_description': '# Drives\n\n[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]\n\nStore your data in seconds.\n\n\n\n\n## Installation\n\n```bash\npip install drives\n```\n\n\n\n## Quickstart\n\n```python\nimport drives\n```\n\n\n\n## License\n\n**Drives** has a BSD-3-Clause license, as found in the [LICENSE](https://github.com/imyizhang/drives/blob/main/LICENSE) file.\n\n\n\n## Contributing\n\nThanks for your interest in contributing to **Drives**! Please feel free to create a pull request.\n\n\n\n## Changelog\n\n**Drives 0.0.1**\n\n* Initial release\n\n\n\n[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label\n[github_link]: https://github.com/imyizhang/drives\n\n\n\n[pypi_badge]: https://badgen.net/pypi/v/drives?icon=pypi&color=black&label\n[pypi_link]: https://www.pypi.org/project/drives',
    'author': 'Yi Zhang',
    'author_email': 'yizhang.dev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/drives',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
