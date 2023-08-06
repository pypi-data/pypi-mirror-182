# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ntc_templates']

package_data = \
{'': ['*'], 'ntc_templates': ['templates/*']}

install_requires = \
['textfsm>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'ntc-templates',
    'version': '3.2.0',
    'description': "TextFSM Templates for Network Devices, and Python wrapper for TextFSM's CliTable.",
    'long_description': '# NTC Templates\n\n<p align="center">\n  <img src="https://raw.githubusercontent.com/networktocode/ntc-templates/master/docs/images/icon-ntc-templates.png" class="logo" height="200px">\n  <br>\n  <a href="https://github.com/networktocode/ntc-templates/actions"><img src="https://github.com/networktocode/ntc-templates/actions/workflows/ci.yml/badge.svg?branch=main"></a>\n  <a href="https://ntc-templates.readthedocs.io/en/latest"><img src="https://readthedocs.org/projects/ntc-templates/badge/"></a>\n  <a href="https://pypi.org/project/ntc-templates/"><img src="https://img.shields.io/pypi/v/ntc-templates"></a>\n  <a href="https://pypi.org/project/ntc-templates/"><img src="https://img.shields.io/pypi/dm/ntc-templates"></a>\n  <br>\n</p>\n\n## Overview\n\nRepository of TextFSM Templates for Network Devices, and Python wrapper for TextFSM\'s CliTable. TextFSM is a tool to help make parsing cli commands more manageable.\n\n## Documentation\n\nFull web-based HTML documentation for this library can be found over on the [NTC Templates Docs](https://ntc-templates.readthedocs.io) website:\n\n- [User Guide](https://ntc-templates.readthedocs.io/en/latest/user/lib_overview/) - Overview, Using the library, Getting Started.\n- [Administrator Guide](https://ntc-templates.readthedocs.io/en/latest/admin/install/) - How to Install, Configure, Upgrade, or Uninstall the library.\n- [Developer Guide](https://ntc-templates.readthedocs.io/en/latest/dev/contributing/) - Extending the library, Code Reference, Contribution Guide.\n- [Release Notes / Changelog](https://ntc-templates.readthedocs.io/en/latest/admin/release_notes/).\n- [Frequently Asked Questions](https://ntc-templates.readthedocs.io/en/latest/user/faq/).\n\n### Contributing to the Docs\n\nAll the Markdown source for the library documentation can be found under the [docs](https://github.com/networktocode/ntc-templates/tree/develop/docs) folder in this repository. For simple edits, a Markdown capable editor is sufficient - clone the repository and edit away.\n\nIf you need to view the fully generated documentation site, you can build it with [mkdocs](https://www.mkdocs.org/). A container hosting the docs will be started using the invoke commands (details in the [Development Environment Guide](https://ntc-templates.readthedocs.io/en/latest/dev/dev_environment/#docker-development-environment)) on [http://localhost:8001](http://localhost:8001). As your changes are saved, the live docs will be automatically reloaded.\n\nAny PRs with fixes or improvements are very welcome!\n\n## Questions\n\nFor any questions or comments, please check the [FAQ](https://ntc-templates.readthedocs.io/en/latest/user/faq/) first. Feel free to also swing by the [Network to Code Slack](https://networktocode.slack.com/) (channel `#networktocode`), sign up [here](http://slack.networktocode.com/) if you don\'t have an account.\n',
    'author': 'Network to Code',
    'author_email': 'info@networktocode.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ntc-templates.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
