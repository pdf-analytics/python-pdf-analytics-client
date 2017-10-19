.. default-role:: code

============
Introduction
============

Purpose
=======

The purpose of PyPDFAnalyticsClient is to provide a library that would help you to automate most common **PDFAnalytics**
using its REST API.

PyPDFAnalyticsClient can verify :
- *textural content*, like text, font style, its location (using coordinates and page number)
- *image content* based on a locally stored image (pixel-by-pixel comparison), its actual size and location in the PDF

Examples
========

This example asserts there is the *figure.png* image on page 4 inside the *demo.pdf* PDF file.

.. code:: python

    >>> from pdf_analytics_client import APIClient
    >>> analytics_server = APIClient(token='my_token')
    >>> new_pdf_job = analytics_server.create_job(local_file='/Users/tester/demo.pdf')
    >>> new_pdf_job.assertImage(local_img='/Users/tester/figure.png', coords={'top':24,'left':64, 'page':4})


Dependencies
============


PyPDFAnalyticsClient has only one dependency **requests**
On Windows, PyAutoGUI has no dependencies (other than Pillow and some other modules, which are installed by pip along with PyAutoGUI). It does **not** need the ``pywin32`` module installed since it uses Python's own ``ctypes`` module.

On OS X, PyAutoGUI requires PyObjC_ installed for the AppKit and Quartz modules. The module names on PyPI to install are ``pyobjc-core`` and ``pyobjc`` (in that order).

.. _PyObjC: http://pythonhosted.org/pyobjc/install.html

On Linux, PyAutoGUI requires ``python-xlib`` (for Python 2) or ``python3-Xlib`` (for Python 3) module installed.

