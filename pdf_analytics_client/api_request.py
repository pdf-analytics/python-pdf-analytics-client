#!/usr/bin/env python
"""
PDFAnalytics API binding

A low level module that handles the HTTP request calls.

Usage :
from pdf_analytics_client import APIRequest
"""
import requests
import base64
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIRequest(object):
    """Basic API client class"""

    def __init__(self, token):
        self.token = token
        #self.__url = 'https://pdf-analytics.com/api/'
        self.__url = 'http://localhost:8000/api/'

    def send_get(self, uri, json=None):
        """ Send GET
        Issues a GET request (read) against the API and returns the result (as Python dict).

        :param uri: The API method to call including parameters
        :return: the result (as Python dict)
        """
        return self.__send_request('GET', uri=uri, json=json)

    def send_post(self, uri, data=None, ofile=None, json=None):
        """Send POST

        Issues a POST request (write) against the API

        :param uri: The API method to call including parameters
        :param data: The data to submit as part of the request (as Python dict, strings must be UTF-8 encoded)
        :param file: the file to be uploaded
        :param json: the json object to be uploaded
        :return: the result (as Python dict)
        """
        return self.__send_request('POST', uri=uri, data=data, ofile=ofile, json=json)

    def __send_request(self, method, uri, data=None, ofile=None, json=None):

        # Get the headers
        headers = {'Authorization': 'Token {token}'.format(token=self.token)}
        if json:
            headers.update({'Content-Type': 'application/json; charset=UTF-8'})
        else:
            headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})

        #if ofile:
        #    headers['Content-Type'] = 'multipart/form-data'
        print('HEREERERERE')
        print(ofile)

        # Make the request
        url = self.__url + uri
        if method == 'POST':
            api_request = requests.post(url, headers=headers, files=ofile, verify=False)
        elif method == 'GET':
            api_request = requests.get(url, headers=headers, verify=False)
        else:
            raise Exception('Method not found')

        if api_request.status_code != 200:
            print('Error in API request: {text}'.format(text=api_request.text))
        #if 'Invalid token' in api_request.text:


        return api_request.status_code, api_request.text