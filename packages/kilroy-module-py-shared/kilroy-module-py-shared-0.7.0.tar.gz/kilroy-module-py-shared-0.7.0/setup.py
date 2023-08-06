# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_module_py_shared', 'kilroy_module_py_shared.resources']

package_data = \
{'': ['*']}

install_requires = \
['betterproto>=2.0.0b5,<3.0.0',
 'jsonschema>=4.7,<5.0',
 'pydantic>=1.9,<2.0',
 'pyhumps>=3.7,<4.0']

setup_kwargs = {
    'name': 'kilroy-module-py-shared',
    'version': '0.7.0',
    'description': 'shared code for kilroy module SDKs in Python 🤝',
    'long_description': '<h1 align="center">kilroy-module-py-shared</h1>\n\n<div align="center">\n\nshared code for kilroy module SDKs in Python 🤝\n\n[![Lint](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/lint.yaml)\n[![Tests](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/test-multiplatform.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Overview\n\nThis package contains code shared by SDKs related to modules.\nMostly it\'s just a bunch of utilities and dataclasses.\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-module-py-shared\n```\n\n## Messages\n\nMessages are dataclasses that are used in the APIs.\nThey are automatically generated from the protobuf definitions.\n\n## Posts\n\nPosts are `pydantic` models that are used to represent various types of posts.\nThere are definitions for:\n\n- `TextOnlyPost`\n- `ImageOnlyPost`\n- `TextAndImagePost`\n- `TextOrImagePost`\n- `TextWithOptionalImagePost`\n- `ImageWithOptionalTextPost`\n\n## Models\n\nOne useful thing this package provides is a `SerializableModel` class.\nIt\'s a base class for `pydantic` models\nthat can be serialized to and from JSON\nwith a proper case convention.\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-module-py-shared',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
