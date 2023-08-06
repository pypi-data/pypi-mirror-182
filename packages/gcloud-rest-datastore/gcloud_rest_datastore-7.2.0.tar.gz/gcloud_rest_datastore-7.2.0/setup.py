# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gcloud', 'gcloud.rest', 'gcloud.rest.datastore']

package_data = \
{'': ['*']}

install_requires = \
['gcloud-rest-auth>=3.1.0,<5.0.0']

setup_kwargs = {
    'name': 'gcloud-rest-datastore',
    'version': '7.2.0',
    'description': 'Python Client for Google Cloud Datastore',
    'long_description': '(Asyncio OR Threadsafe) Python Client for Google Cloud Datastore\n================================================================\n\n    This is a shared codebase for ``gcloud-rest-datastore`` and\n    ``gcloud-rest-datastore``\n\n|pypi| |pythons-aio| |pythons-rest|\n\nInstallation\n------------\n\n.. code-block:: console\n\n    $ pip install --upgrade gcloud-{aio,rest}-datastore\n\nUsage\n-----\n\nSee `our docs`_.\n\nContributing\n------------\n\nPlease see our `contributing guide`_.\n\n.. _contributing guide: https://github.com/talkiq/gcloud-rest/blob/master/.github/CONTRIBUTING.rst\n.. _our docs: https://talkiq.github.io/gcloud-rest\n\n.. |pypi| image:: https://img.shields.io/pypi/v/gcloud-rest-datastore.svg?style=flat-square\n    :alt: Latest PyPI Version (gcloud-rest-datastore)\n    :target: https://pypi.org/project/gcloud-rest-datastore/\n\n.. |pythons-aio| image:: https://img.shields.io/pypi/pyversions/gcloud-rest-datastore.svg?style=flat-square&label=python (aio)\n    :alt: Python Version Support (gcloud-rest-datastore)\n    :target: https://pypi.org/project/gcloud-rest-datastore/\n\n.. |pythons-rest| image:: https://img.shields.io/pypi/pyversions/gcloud-rest-datastore.svg?style=flat-square&label=python (rest)\n    :alt: Python Version Support (gcloud-rest-datastore)\n    :target: https://pypi.org/project/gcloud-rest-datastore/\n',
    'author': 'Vi Engineering',
    'author_email': 'voiceai-eng@dialpad.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/talkiq/gcloud-aio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
}


setup(**setup_kwargs)
