`ffmpegio-plugin-downloader`: An `ffmpegio` plugin to download latest FFmpeg release binaries
=============================================================================================

|pypi| |pypi-status| |pypi-pyvers| |github-license| |github-status|

.. |pypi| image:: https://img.shields.io/pypi/v/ffmpegio
  :alt: PyPI
.. |pypi-status| image:: https://img.shields.io/pypi/status/ffmpegio
  :alt: PyPI - Status
.. |pypi-pyvers| image:: https://img.shields.io/pypi/pyversions/ffmpegio
  :alt: PyPI - Python Version
.. |github-license| image:: https://img.shields.io/github/license/python-ffmpegio/python-ffmpegio
  :alt: GitHub License
.. |github-status| image:: https://img.shields.io/github/workflow/status/python-ffmpegio/python-ffmpegio/Run%20Tests
  :alt: GitHub Workflow Status

Python `ffmpegio` package aims to bring the full capability of `FFmpeg <https://ffmpeg.org>`__
to read, write, and manipulate multimedia data to Python. FFmpeg is an open-source cross-platform 
multimedia framework, which can handle most of the multimedia formats available today.

`ffmpegio-plugin-downloader` adds a capability to download the latest release build of 
FFmpeg via officially acknowledged host servers.

.. code-block:: bash

  pip install ffmpegio-core # or ffmpegio if using it with its NumPy interface

  pip install ffmpegio_plugin_downloader

  python -m ffmpeg_downloader # downloads and installs the latest release

Documentation
-------------

Visit our `GitHub page here <https://python-ffmpegio.github.io/python-ffmpegio/>`__
