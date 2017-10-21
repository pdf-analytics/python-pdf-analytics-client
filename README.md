# python-pdf-analytics-client

<a href='http://pdf-analytics-client-library.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/pdf-analytics-client-library/badge/?version=latest' alt='Documentation Status' />
</a>
      
      
PDF Analytics client API library

PDF Analytics is a web service which lets you use to verify PDF content for free. 

This library allows you to automate most common PDF Analytics operations using Python 3.6.

- Ability to create PDF (analysis) job, what would upload a PDF file to the platform
- Ability to *verify textural content* from a PDF 
  * verify the text
  * verify the text font style, and
  * verify its location, using coordinates and page number
- Ability to *verify image content* from a PDF
  * get the expected image from the PDF
  * compare a local saved image with the one in the PDF pixel-by-pixel comparison
  * verify the image size in the PDF
  
There are are two ways to verify a PDF content.

1. To verify directly the PDF content

2. (In future) To verify the PDF content based on a template


```python
from pdf_analytics_client import APIClient

# Connect to the Server
analytics_server = APIClient(token='my_token')

# Create a PDF analysis job
pdf_job = analytics_server.create_job(local_file='/Users/tester/demo.pdf')

# Assert an image on page 4
pdf_job.assertImage(local_img='/Users/tester/figure.png', coords={'top':24,'left':64}, page=4)

# Assert the same image in every page
pdf_job.assertImage(local_img='/Users/tester/figure.png', coords={'top':24,'left':64}, page='all')

# Assert the same image in page 2,4
pdf_job.assertImage(local_img='/Users/tester/figure.png', coords={'top':24,'left':64}, page=[2,4])

# Assert text content in page 2
pdf_job.assertText(text='This is a simple text', coords={'top':24,'left':64}, page=2)

# Assert text content and font
pdf_job.assertText(text='This is a simple text', coords={'top':24,'left':64}, page=2, font='Arial, Bold')

```


# Install

```
pip install python-pdf-analytics-client (TODO)
```
