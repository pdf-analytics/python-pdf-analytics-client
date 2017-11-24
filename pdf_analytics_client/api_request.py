#!/usr/bin/env python
"""
PDFAnalytics API binding

A low level module that handles the HTTP request calls.

Usage :
from pdf_analytics_client import APIRequest
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import json
import requests


class APIRequest(object):
    """Basic API client class"""

    def __init__(self, token, url):
        self.token = token
        self.__url = url

    def send_get(self, uri, data=None, ojson=None):
        """ Send GET
        Issues a GET request (read) against the API and returns the result (as Python dict).

        :param uri: The API method to call including parameters
        :return: the result (as Python dict)
        """
        return self.__send_request('GET', uri=uri, data=data, ojson=ojson)

    def send_post(self, uri, data=None, ofile=None, ojson=None):
        """Send POST

        Issues a POST request (write) against the API

        :param uri: The API method to call including parameters
        :param data: The data to submit as part of the request (as Python dict, strings must be UTF-8 encoded)
        :param file: the file to be uploaded
        :param json: the json object to be uploaded
        :return: the result (as Python dict)
        """
        return self.__send_request('POST', uri=uri, data=data, ofile=ofile, ojson=ojson)

    def __send_request(self, method, uri, data=None, ofile=None, ojson=None):
        # Get the headers
        headers = {'Authorization': 'Token {token}'.format(token=self.token)}

        if ojson:
            headers.update({'Content-Type': 'application/json; charset=UTF-8'})

        # Make the request
        url = self.__url + uri
        if method == 'POST':
            api_request = requests.post(url, headers=headers, data=data, files=ofile, verify=True)
        elif method == 'GET':
            api_request = requests.get(url, headers=headers, data=data, json=ojson, verify=True)
        else:
            raise Exception('Method not found')

        if api_request.status_code != requests.codes.ok:
            print('Error in API request: {text}'.format(text=api_request.text))

        # Return a json file, if the response is JSON
        try:
            json_object = json.loads(api_request.text)
        except ValueError:
            return api_request.status_code, api_request.text

        return api_request.status_code, json_object

