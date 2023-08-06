# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mgpdf']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'pypdf2>=3.0.0,<4.0.0']

entry_points = \
{'console_scripts': ['mgpdf = mgpdf.mgpdf:cli']}

setup_kwargs = {
    'name': 'mgpdf',
    'version': '0.0.2',
    'description': '',
    'long_description': '# mgpdf\n\n[![PyPI - Version](https://img.shields.io/pypi/v/mgpdf.svg)](https://pypi.org/project/mgpdf)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mgpdf.svg)](https://pypi.org/project/mgpdf)\n\n-----\n\n**Table of Contents**\n\n- [Installation](#installation)\n- [License](#license)\n\n## Installation\n\n```console\npip install mgpdf\n```\n\n## License\n\n`mgpdf` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.\n',
    'author': 'liuxsdev',
    'author_email': '1028330144@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/liuxsdev/mgpdf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
