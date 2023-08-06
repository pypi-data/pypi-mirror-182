papermill_service
===========================

|code_ci| |docs_ci| |coverage| |pypi_version| |license|

This package provides a service-line runner for jupyter notebooks, combining FastAPI and papermill.

============== ==============================================================
PyPI           ``pip install papermill_service``
Source code    https://github.com/garryod/papermill_service
Documentation  https://garryod.github.io/papermill_service
Releases       https://github.com/garryod/papermill_service/releases
============== ==============================================================

To start the service, simply run::

    $ NOTEBOOK_PATH=/path/to/notebook.ipynb python -m papermill_service

To view the API docs navigate to :code:`http://localhost:8000/docs`

.. |code_ci| image:: https://github.com/garryod/papermill_service/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/garryod/papermill_service/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/garryod/papermill_service/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/garryod/papermill_service/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/garryod/papermill_service/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/garryod/papermill_service
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/papermill_service.svg
    :target: https://pypi.org/project/papermill_service
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://garryod.github.io/papermill_service for more detailed documentation.
