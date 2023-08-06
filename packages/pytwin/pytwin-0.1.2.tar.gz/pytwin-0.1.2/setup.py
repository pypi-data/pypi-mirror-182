# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src/ansys'}

packages = \
['pytwin',
 'pytwin.evaluate',
 'pytwin.examples',
 'pytwin.twin_runtime',
 'pytwin.twin_runtime.linux64',
 'pytwin.twin_runtime.win64']

package_data = \
{'': ['*'],
 'pytwin.twin_runtime': ['licensingclient/linx64/*',
                         'licensingclient/winx64/*',
                         'messages/*']}

install_requires = \
['numpy==1.23.4', 'pandas==1.5.1']

extras_require = \
{':platform_system == "Windows"': ['pywin32>=304'],
 ':python_version < "3.8"': ['importlib-metadata>=4.0,<5.0']}

setup_kwargs = {
    'name': 'pytwin',
    'version': '0.1.2',
    'description': 'A python wrapper for Ansys Digital Twin components',
    'long_description': 'Pytwin\n======\n|pyansys| |python| |pypi| |codecov| |GH-CI| |MIT| |black|\n\n.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC\n   :target: https://docs.pyansys.com/\n   :alt: PyAnsys\n\n.. |python| image:: https://img.shields.io/badge/Python-%3E%3D3.9-blue\n   :target: https://pypi.org/project/pytwin/\n   :alt: Python\n\n.. |pypi| image:: https://img.shields.io/pypi/v/pytwin-library.svg?logo=python&logoColor=white\n   :target: https://pypi.org/project/pytwin/\n   :alt: PyPI\n\n.. |codecov| image:: https://codecov.io/gh/pyansys/pytwin/branch/main/graph/badge.svg\n   :target: https://codecov.io/gh/pyansys/pytwin/\n   :alt: Codecov\n\n.. |GH-CI| image:: https://github.com/pyansys/pytwin/actions/workflows/ci.yml/badge.svg\n   :target: https://github.com/pyansys/pytwin/actions/workflows/ci.yml\n   :alt: GH-CI\n\n.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg\n   :target: https://opensource.org/licenses/MIT\n   :alt: MIT\n\n.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat\n   :target: https://github.com/psf/black\n   :alt: Black\n\nOverview\n--------\nPyTwin is a Python package that eases `Ansys Digital Twins`_ consumption workflows.\n\n\nDocumentation\n-------------\nFor comprehensive information on PyTwin, see the latest release `Documentation`_\nand its sections:\n\n* `Getting started`_\n* `User guide`_\n* `API reference`_\n* `Examples`_\n* `Contributing`_\n\nInstallation\n------------\nThe ``pytwin`` package supports Python 3.8 through Python\n3.10 on Windows and Linux.\n\nInstall the latest release from `PyPI\n<https://pypi.org/project/pytwin/>`_ with:\n\n.. code:: console\n\n    pip install pytwin\n\nIf you plan on doing local *development* of PyTwin with Git, install\nthe latest release with:\n\n.. code:: console\n\n    git clone https://github.com/pyansys/pytwin.git\n    cd pytwin\n    pip install pip -U\n    pip install -e .\n\nDependencies\n------------\nThe ``pytwin`` package requires access to an Ansys License Server\nwith the ``twin_builder_deployer`` feature available (see the\n`Getting started`_ section).\n\n\nLicense and acknowledgments\n---------------------------\nPyTwin is licensed under the MIT license.\n\nFor more information on `Ansys Digital Twins`_, see the `Twin Builder`_\npage on the Ansys website.\n\n.. LINKS AND REFERENCES\n.. _Ansys Digital Twins: https://www.ansys.com/products/digital-twin/\n.. _Twin Builder: https://www.ansys.com/products/digital-twin/ansys-twin-builder\n.. _Documentation: https://twin.docs.pyansys.com/\n.. _Getting started: https://twin.docs.pyansys.com/release/0.1/getting_started/index.html\n.. _User guide: https://twin.docs.pyansys.com/release/0.1/user_guide/index.html\n.. _API reference: https://twin.docs.pyansys.com/release/0.1/api/index.html\n.. _Examples: https://twin.docs.pyansys.com/release/0.1/examples/index.html\n.. _Contributing: https://twin.docs.pyansys.com/release/0.1/contributing.html\n',
    'author': 'ANSYS, Inc.',
    'author_email': 'ansys.support@ansys.com',
    'maintainer': 'PyAnsys developers',
    'maintainer_email': 'pyansys.maintainers@ansys.com',
    'url': 'https://github.com/pyansys/pytwin',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
