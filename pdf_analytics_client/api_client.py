#!/usr/bin/env python
"""
---------------------
 PDF Analytics Client
---------------------

The PDF Analytics Client is a high level module that enables the verification of the images and text of a
local PDF file.

"""
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import time

from api_request import APIRequest


class JobClass:
    """Basic PDF analysis Job class """

    def __init__(self, id, client):
        self.id = id
        self.__client = client

    def wait_analysis_to_complete(self):
        """Wait for the PDF analysis to complete

        After you submit the PDF to PDF Analytics website, the takes some seconds until
        it is ready to be used for verification.

        :return: If the analysis is completed and returns *True* else if in 20 seconds the job is
                 not complete, returns *False*
        :rtype: bool

        """
        count = 0
        while self.get_status() == 'In Progress' and count < 10:
            time.sleep(3)
            count += 1

        final_status = self.get_status()
        if final_status == 'In Progress':
            return False
        else:
            return True

    def get_status(self):
        """Get the status of the PDF analysis

        :return: The analysis status as string. The string can be "In progress", "Error" or "Complete"
        :rtype: str
        """
        _, response = self.__client.send_get(uri='job/{id}/get_status/'.format(id=self.id))
        return response['status']

    def verify_image(self, path, left, top, page, compare_method="pbp", tolerance=0.0):
        """ Verify a local image file exists in the PDF

        :param path: The absolute or relative path of the locally stored image e.g. '/User/tester/apple.png'
        :param left: Distance from the *left* of the page in *points*. Accepts single integer. e.g. 150
        :param top: Distance from the *top* of the page in *points*. Accepts single integer. e.g 200
        :param page: Number of page, e.g. an integer 4 or a string 'all', 'last', '1-4'
        :param compare_method: Image comparison method
        :param tolerance: Comparison tolerance. Default value 0.0. Example: 0.02
        :return: If the request is successful it returns 200. If it is not successful it returns the error message.
        :rtype: JSON

        """
        request_json = {
            'id': int(self.id),
            'page': str(page),
            'top': int(top),
            'left': int(left),
            'compare_method': compare_method,
            'tolerance': tolerance
        }

        full_path = os.path.abspath(path)
        file_name = os.path.basename(full_path)
        files = {'image_file': (file_name, open(full_path, 'rb'))}
        status_code, response = self.__client.send_post(uri='job/verify_image/', data=request_json, ofile=files)

        return response

    def verify_pdf(self, path, excluded_areas='', tolerance=0.0):
        """ Verify a local PDF file with the uploaded job's PDF

        :param path: The absolute or relative path of the locally stored PDF ilfe e.g. '/User/tester/report.pdf'
        :param excluded_areas: Excluded areas. List field. Example : [
                               {'left':146, 'top':452, 'width':97, 'height':13,'page':2},
                               {'left': 414, 'top': 747, 'width': 45, 'height': 16, 'page': 'all'},]
        :param tolerance: Comparison tolerance. Default value 0.0. Example: 0.02
        :return: If the request is successful it returns 200. If it is not successful it returns the error message.
        :rtype: JSON
        """
        request_json = {
            'id': int(self.id),
            'excluded_areas': excluded_areas,
            'tolerance': tolerance
        }

        full_path = os.path.abspath(path)
        file_name = os.path.basename(full_path)
        files = {'pdf_file': (file_name, open(full_path, 'rb'))}
        status_code, response = self.__client.send_post(uri='job/verify_pdf/', data=request_json, ofile=files)
        return response

    def verify_text(self, text, left, top, page, method='contains'):
        """ Verify a text exists in the PDF

        :param text: The expected textural content. Accepts string. e.g. 'This is the expected text'
        :param left: Distance from the *left* of the page in *points*. Accepts single integer. e.g. 150
        :param top: Distance from the *top* of the page in *points*. Accepts single integer. e.g 200
        :param page: Number of page, e.g. an integer 4 or a string 'all', 'last', '1-4'
        :param method: Text comparison method
        :return: If the request is successful it returns 200. If it is not successful it returns the error message.
        """
        text_comparison_method = {
            'contains': 'contains',
            'ends_with': 'ends_with',
            'starts_with': 'starts_with',
            'exact_content': 'exact_content'
        }

        request_json = {
            'id': int(self.id),
            'page': str(page),
            'expected_text': str(text),
            'method': text_comparison_method.get(method),
            'top': int(top),
            'left': int(left)
        }

        _, response = self.__client.send_get(uri='job/verify_text/', data=request_json)
        return response

    def get_item(self, left, top, page, type='any'):
        """Get any item from the PDF (TODO: get figure)

        :param left: Distance from the *left* of the page in *points*. Accepts single integer. e.g. 150
        :param top: Distance from the *top* of the page in *points*. Accepts single integer. e.g 200
        :param page: Number of page, e.g. 4
        :param type: Type of the the item.
        :return: A JSON object with the item's information
        """
        request_json = {
            'id': int(self.id),
            'page': int(page),
            'type': type,
            'top': int(top),
            'left': int(left)
        }
        _, response = self.__client.send_get(uri='find_content/', data=request_json)
        return list(response.values())[0]

    def get_metadata(self):
        """Get the metadata of the PDF

        :return: A JSON object with the metadata of the PDF
        """
        _, response = self.__client.send_get(uri='job/{id}/metadata/'.format(id=self.id))
        return response


class APIClient:
    """Main API client class"""

    def __init__(self, token, url='https://pdf-analytics.com/api/'):
        self.client = APIRequest(token=token, url=url)

    def create_job(self, local_file, wait_to_complete=True):
        """Create a PDF analysis job

        :param local_file: the path of the local PDF file that needs to be uploaded to the server for the analysis
        :param wait_to_complete: wait for the PDF analysis to complete. Default value is True.
        :return: The JobClass object,
        """
        file_name = os.path.basename(local_file)
        files = {'file': (file_name, open(local_file, 'rb'))}
        _, response = self.client.send_post(uri='job/upload/', ofile=files)
        job_obj = JobClass(id=int(response['id']), client=self.client)

        if wait_to_complete:
            job_obj.wait_analysis_to_complete()

        return job_obj

    def get_job(self, job_id):
        """Get PDF analysis job

        :param job_id: the PDF analysis job ID
        :return: The JobClass object,
        """
        job_obj = JobClass(id=int(job_id), client=self.client)
        return job_obj

    def get_account_details(self):
        """Get my account details

        :return: a dictionary object with the user's account details
                {   'max_pdf_size_mb': 3,
                'daily_max_count': 10,
                'today_remaining': 4,
                }
        """
        _, response = self.client.send_get(uri='account_details/')
        return response
