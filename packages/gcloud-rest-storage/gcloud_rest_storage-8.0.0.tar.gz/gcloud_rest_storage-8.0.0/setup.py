# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gcloud', 'gcloud.rest', 'gcloud.rest.storage']

package_data = \
{'': ['*']}

install_requires = \
['gcloud-rest-auth>=3.6.0,<5.0.0', 'pyasn1-modules>=0.2.1,<0.3.0']

extras_require = \
{':python_version < "3.0"': ['rsa>=3.1.4,<4.4.0'],
 ':python_version >= "3.7"': ['rsa>=3.1.4,<5.0.0']}

setup_kwargs = {
    'name': 'gcloud-rest-storage',
    'version': '8.0.0',
    'description': 'Python Client for Google Cloud Storage',
    'long_description': '(Asyncio OR Threadsafe) Python Client for Google Cloud Storage\n==============================================================\n\n    This is a shared codebase for ``gcloud-rest-storage`` and\n    ``gcloud-rest-storage``\n\n|pypi| |pythons-aio| |pythons-rest|\n\nInstallation\n------------\n\n.. code-block:: console\n\n    $ pip install --upgrade gcloud-{aio,rest}-storage\n\nUsage\n-----\n\nSee `our docs`_.\n\nContributing\n------------\n\nPlease see our `contributing guide`_.\n\n.. _contributing guide: https://github.com/talkiq/gcloud-rest/blob/master/.github/CONTRIBUTING.rst\n.. _our docs: https://talkiq.github.io/gcloud-rest\n\n.. |pypi| image:: https://img.shields.io/pypi/v/gcloud-rest-storage.svg?style=flat-square\n    :alt: Latest PyPI Version (gcloud-rest-storage)\n    :target: https://pypi.org/project/gcloud-rest-storage/\n\n.. |pythons-aio| image:: https://img.shields.io/pypi/pyversions/gcloud-rest-storage.svg?style=flat-square&label=python (aio)\n    :alt: Python Version Support (gcloud-rest-storage)\n    :target: https://pypi.org/project/gcloud-rest-storage/\n\n.. |pythons-rest| image:: https://img.shields.io/pypi/pyversions/gcloud-rest-storage.svg?style=flat-square&label=python (rest)\n    :alt: Python Version Support (gcloud-rest-storage)\n    :target: https://pypi.org/project/gcloud-rest-storage/\n',
    'author': 'Vi Engineering',
    'author_email': 'voiceai-eng@dialpad.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/talkiq/gcloud-aio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
}


setup(**setup_kwargs)
