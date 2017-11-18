.. default-role:: code

============
Introduction
============

Purpose
=======

The purpose of python-pdf-analytics-client is to provide a library that would help you to automate most common **PDFAnalytics**
using its REST API.

python-pdf-analytics-client can verify :

- *textural content*, like text, font style, its location (using coordinates and page number)

- *image content* based on a locally stored image (pixel-by-pixel comparison),
  its actual size and location in the PDF

- *pdf-to-pdf* comparison, compare an uploaded PDF with a local one pixel-by-pixel, page-by-page

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

**python-pdf-analytics-client** has only one dependency `python-requests <http://docs.python-requests.org/en/master/user/install/>`_ .
All the dependencies shall be installed automatically when you will install the **python-pdf-analytics-client** module with pip.

Examples
========

You may find the examples at the GitHub repository : https://github.com/pdf-analytics/python-pdf-analytics-client/tree/master/examples

To run the **examples** you need to have registered to the site pdf-analytics and to get your token number.

To run the examples:

.. code-block:: python

   $ cd examples
   # Install the dependecies
   $ pip install -r requirements_examples
   # Run the examples
   $ behave -D token=<your_token_id>

