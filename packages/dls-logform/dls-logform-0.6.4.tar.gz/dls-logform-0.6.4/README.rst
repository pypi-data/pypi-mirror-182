dls-logform
===========================

|code_ci| |docs_ci| |coverage| |pypi_version| |anaconda_version| |license|


Formats Python log messages by overriding the Python logging.Formatter class.

description
-------------------------------------------------
- a library to enable enhanced log formatting
- foundation for even more improvements to log formatting

use cases
-------------------------------------------------
- developer wants to provide end user with easily readable messags
- many developers working on many programs and device servers want to unify output format
- operations person running a pipeline with multiple running processes needs to combine logs using same format
- logging server needs index-able fields without grokking

implementation
-------------------------------------------------
- ses python standard logging
- custom formatter overrides logging.Formatter to give time, process, source file and message on a single line
- if requested, it also adds custom fields for consumption by the logging server


example output
-------------------------------------------------
::

    2022-12-15 11:51:12.717976 20228 billy-datafa main             5397        1 DEBUG     /dls_sw/apps/bxflow/pippy_place/dls-bxflow/1.11.0/dls_billy_lib/databases/aiosqlite.py[418] 1 rows from UPDATE cookies SET contents = ? WHERE uuid = 'f762d50e-acb7-4287-b95d-da5ae64075b3'
    2022-12-15 12:01:33.329887 20495 bx_gui       main           622823   620683 ERROR     /home/kbp43231/.local/lib/python3.9/site-packages/aiohttp/web_protocol.py[405] Error handling request
                                                                                 EXCEPTION BadStatusLine: 400, message="Bad status line 'Invalid method encountered'"
                                                                                 TRACEBACK /home/kbp43231/.local/lib/python3.9/site-packages/aiohttp/web_protocol.py[334] messages, upgraded, tail = self._request_parser.feed_data(data)
                                                                                 TRACEBACK aiohttp/_http_parser.pyx[551]
    2022-12-15 12:23:49.551657 20495 bx_gui       main          1959045  1336221 DEBUG     /dls_sw/apps/bxflow/pippy_place/dls-bxflow/1.11.0/dls_billy_lib/base_aiohttp.py[514] [COOKOFF] registering cookies ['BXFLOW_TABS_MANAGER']

example code
-------------------------------------------------
    .. code-block:: python

        import logging

        from dls_logform.dls_logform import DlsLogform

        # Make handler which writes the logs to console.
        handler = logging.StreamHandler()

        # Make the formatter from this library.
        dls_logform = DlsLogform()

        # Let handler write the custom formatted messages.
        handler.setFormatter(dls_logform)

        # Let root logger use the handler.
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)

============== ==============================================================
PyPI           ``pip install dls-logform``
Conda          ``conda install -c dae-dls dls-logform``
Source code    https://github.com/dae-dls/dls-logform
Documentation  https://dae-dls.github.io/dls-logform
Releases       https://github.com/dae-dls/dls-logform/releases
============== ==============================================================

To check the version of the library, you can run this command::

    $ python -m dls_logform --version

.. |code_ci| image:: https://github.com/dae-dls/dls-logform/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/dae-dls/dls-logform/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/dae-dls/dls-logform/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/dae-dls/dls-logform/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/dae-dls/dls-logform/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/dae-dls/dls-logform
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/dls-logform.svg
    :target: https://pypi.org/project/dls-logform
    :alt: Latest PyPI version

.. |anaconda_version| image:: https://anaconda.org/dae-dls/dls-logform/badges/version.svg
    :target: https://anaconda.org/dae-dls/dls-logform
    :alt: Latest Anaconda version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://dae-dls.github.io/dls-logform for more detailed documentation.
