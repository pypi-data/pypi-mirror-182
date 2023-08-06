# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_module_client_py_sdk', 'kilroy_module_client_py_sdk.resources']

package_data = \
{'': ['*']}

install_requires = \
['aiostream>=0.4,<0.5', 'kilroy-module-py-shared>=0.7,<0.8']

setup_kwargs = {
    'name': 'kilroy-module-client-py-sdk',
    'version': '0.9.0',
    'description': 'SDK for kilroy module clients in Python 🧰',
    'long_description': '<h1 align="center">kilroy-module-client-py-sdk</h1>\n\n<div align="center">\n\nSDK for kilroy module clients in Python 🧰\n\n[![Lint](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/lint.yaml)\n[![Tests](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/test-multiplatform.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-module-client-py-sdk\n```\n\n## Usage\n\n```python\nfrom kilroy_module_client_py_sdk import ModuleService\n\nservice = ModuleService(host="localhost", port=11000)\n\nawait service.get_metadata()\n```\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-module-client-py-sdk',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
