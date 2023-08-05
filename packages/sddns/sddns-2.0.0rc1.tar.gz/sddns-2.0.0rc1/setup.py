# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sddns']

package_data = \
{'': ['*']}

install_requires = \
['octodns>=0.9.21,<0.10.0']

setup_kwargs = {
    'name': 'sddns',
    'version': '2.0.0rc1',
    'description': 'Build DNS records by Python scripts',
    'long_description': '# Software Defined DNS (SD-DNS)\nBuild DNS records by Python scripts. This script can gernerate yaml for OctoDNS.\n\nUsage can be found in https://github.com/baobao1270/sddns-template\n\n## License\nMIT\n',
    'author': 'Joseph Chris',
    'author_email': 'joseph@josephcz.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/baobao1270/sddns.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
