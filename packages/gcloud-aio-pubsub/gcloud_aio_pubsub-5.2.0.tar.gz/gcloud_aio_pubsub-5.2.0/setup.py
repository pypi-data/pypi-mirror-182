# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gcloud', 'gcloud.aio', 'gcloud.aio.pubsub']

package_data = \
{'': ['*']}

install_requires = \
['gcloud-aio-auth>=3.3.0,<5.0.0', 'prometheus-client>=0.13.1,<1.0.0']

setup_kwargs = {
    'name': 'gcloud-aio-pubsub',
    'version': '5.2.0',
    'description': 'Python Client for Google Cloud Pub/Sub',
    'long_description': '(Asyncio OR Threadsafe) Python Client for Google Cloud Pub/Sub\n==============================================================\n\n    This is a shared codebase for ``gcloud-aio-pubsub`` and\n    ``gcloud-rest-pubsub``\n\n|pypi| |pythons-aio| |pythons-rest|\n\nInstallation\n------------\n\n.. code-block:: console\n\n    $ pip install --upgrade gcloud-{aio,rest}-pubsub\n\nUsage\n-----\n\nSee `our docs`_.\n\nContributing\n------------\n\nPlease see our `contributing guide`_.\n\n.. _contributing guide: https://github.com/talkiq/gcloud-aio/blob/master/.github/CONTRIBUTING.rst\n.. _our docs: https://talkiq.github.io/gcloud-aio\n\n.. |pypi| image:: https://img.shields.io/pypi/v/gcloud-aio-pubsub.svg?style=flat-square\n    :alt: Latest PyPI Version\n    :target: https://pypi.org/project/gcloud-aio-pubsub/\n\n.. |pythons-aio| image:: https://img.shields.io/pypi/pyversions/gcloud-aio-pubsub.svg?style=flat-square&label=python (aio)\n    :alt: Python Version Support (gcloud-aio-pubsub)\n    :target: https://pypi.org/project/gcloud-aio-pubsub/\n\n.. |pythons-rest| image:: https://img.shields.io/pypi/pyversions/gcloud-rest-pubsub.svg?style=flat-square&label=python (rest)\n    :alt: Python Version Support (gcloud-rest-pubsub)\n    :target: https://pypi.org/project/gcloud-rest-pubsub/\n',
    'author': 'Vi Engineering',
    'author_email': 'voiceai-eng@dialpad.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/talkiq/gcloud-aio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
