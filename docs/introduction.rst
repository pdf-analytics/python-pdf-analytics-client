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
    >>> server = APIClient(token='my_token')
    >>> pdf_job = server.create_job(local_file='/Users/tester/demo.pdf')
    >>> pdf_job.verify_image(local_img='/Users/tester/figure.png', top=24, left=64, page=4)


Dependencies
============


PyPDFAnalyticsClient has only one dependency `python-requests <http://docs.python-requests.org/en/master/user/install/>`_ .

To run the **examples** you need also the `python-behave <http://pythonhosted.org/behave//>`_ . To install all dependencies :

.. code-block:: python

   pip install requirements

