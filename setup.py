from distutils.core import setup

setup(
    name='python-pdf-analytics-client',
    version='1.0.5',
    packages=['pdf_analytics_client'],
    url='https://pdf-analytics.com',
    license='MIT License ',
    author='PDF Analytics',
    author_email='info@pdf-analytics.com',
    download_url='https://github.com/pdf-analytics/python-pdf-analytics-client',
    keywords='testing pdf inspection python automated testing software testing pdf-analytics.com',
    classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Testing',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',

    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Unix',
],
    description='PyPDFAnalyticsClient allows you to automate most common PDFAnalytics (https://pdf-analytics.com) operations using Python 2 or Python 3. ',
    long_description="PyPDFAnalyticsClient allows you to automate most common PDFAnalytics (https://pdf-analytics.com) operations using Python 2 or Python 3. You may access the documentation page from here : http://pdf-analytics-client-library.readthedocs.io/en/latest/. You may access the GitHub repository from here : https://github.com/pdf-analytics/python-pdf-analytics-client ."

)
