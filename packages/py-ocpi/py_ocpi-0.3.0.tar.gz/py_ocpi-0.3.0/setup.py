# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_ocpi',
 'py_ocpi.core',
 'py_ocpi.modules',
 'py_ocpi.modules.cdrs',
 'py_ocpi.modules.cdrs.v_2_2_1',
 'py_ocpi.modules.cdrs.v_2_2_1.api',
 'py_ocpi.modules.commands',
 'py_ocpi.modules.commands.v_2_2_1',
 'py_ocpi.modules.commands.v_2_2_1.api',
 'py_ocpi.modules.credentials',
 'py_ocpi.modules.credentials.v_2_2_1',
 'py_ocpi.modules.credentials.v_2_2_1.api',
 'py_ocpi.modules.locations',
 'py_ocpi.modules.locations.v_2_2_1',
 'py_ocpi.modules.locations.v_2_2_1.api',
 'py_ocpi.modules.sessions',
 'py_ocpi.modules.sessions.v_2_2_1',
 'py_ocpi.modules.sessions.v_2_2_1.api',
 'py_ocpi.modules.tariffs',
 'py_ocpi.modules.tariffs.v_2_2_1',
 'py_ocpi.modules.tariffs.v_2_2_1.api',
 'py_ocpi.modules.tokens',
 'py_ocpi.modules.tokens.v_2_2_1',
 'py_ocpi.modules.tokens.v_2_2_1.api',
 'py_ocpi.modules.versions',
 'py_ocpi.modules.versions.api',
 'py_ocpi.routers',
 'py_ocpi.routers.v_2_2_1']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.68.0,<0.69.0', 'httpx>=0.23.0,<0.24.0']

setup_kwargs = {
    'name': 'py-ocpi',
    'version': '0.3.0',
    'description': 'Python Implementation of OCPI',
    'long_description': '\n.. image:: https://img.shields.io/pypi/v/py-ocpi.svg?style=flat\n   :target: https://pypi.org/project/py-ocpi/\n.. image:: https://pepy.tech/badge/py-ocpi/month\n   :target: https://pepy.tech/project/py-ocpi\n.. image:: https://github.com/TECHS-Technological-Solutions/ocpi/actions/workflows/pypi.yaml/badge.svg?style=svg\n   :target: https://github.com/TECHS-Technological-Solutions/ocpi/actions?query=workflow:pypi\n.. image:: https://coveralls.io/repos/github/TECHS-Technological-Solutions/ocpi/badge.svg\n   :target: https://coveralls.io/github/TECHS-Technological-Solutions/ocpi\n   \nIntroduction\n============\n\nThis Library is a Python implementation of the Open Charge Point Interface (OCPI)\n\n\nGetting Started\n===============\n\nInstallation\n------------\n\ninstall Py-OCPI like this:\n\n.. code-block:: bash\n\n    pip install py-ocpi\n\n\nHow Does it Work?\n-----------------\n\nModules that communicate with central system will use crud for retrieving required data. the data that is retrieved from central system may\nnot be compatible with OCPI protocol. So the data will be passed to adapter to make it compatible with schemas defined by OCPI. User only needs to\nmodify crud and adapter based on central system architecture.\n\nExample\n-------\n\nhttps://github.com/TECHS-Technological-Solutions/ocpi/blob/830dba5fb3bbc7297326a4963429d7a9f850f28d/examples/v_2_2_1.py#L1-L205\n\nDocuments\n---------\n\nCheck the `Documentation <https://techs-technological-solutions.github.io/ocpi/>`_\n\n\nLicense\n=======\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'HAkhavan71',
    'author_email': 'hakh.27@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TECHS-Technological-Solutions/ocpi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
