#!/usr/bin/env python
"""
---------------------
 PDF Analytics Client
---------------------

The PDF Analytics Client is a high level module that enables the verification of the images and text of a
local PDF file.

"""
import os
import time

from pdf_analytics_client.api_request import APIRequest


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
        """
        _, response = self.__client.send_get(uri='job/{id}/get_status/'.format(id=self.id))
        return response['status']

    def verify_image(self, path, left, top, page, compare_method="pbp", tolerance=0.0):
        """ Verify a local image file exists in the PDF

        :param path: The absolute or relative path of the locally stored image e.g. '/User/tester/apple.png'
        :param left: Distance from the *left* of the page in *points*. Accepts single integer. e.g. 150
        :param top: Distance from the *top* of the page in *points*. Accepts single integer. e.g 200
        :param page: Number of page, e.g. 4
        :param compare_method: Image comparison method
        :param tolerance: Comparison tolerance. Default value 0.0. Example: 0.02
        :return: If the Returns in JSON the image item.
        """
        request_json = {
            'id': int(self.id),
            'page': int(page),
            'top': int(top),
            'left': int(left),
            'compare_method': compare_method,
            'tolerance': tolerance
        }

        full_path = os.path.abspath(path)
        file_name = os.path.basename(full_path)
        files = {'image_file': (file_name, open(full_path, 'rb'))}
        status_code, response = self.__client.send_post(uri='job/verify_image/', data=request_json, ofile=files)

        if status_code != 200:
            raise Exception(response)

        return response

    def verify_text(self, text, left, top, page):
        """ Verify a text exists in the PDF (TODO)

        :param text: The text content. Accepts string. e.g. 'This is a document'
        :param left: Distance from the *left* of the page in *points*. Accepts single integer. e.g. 150
        :param top: Distance from the *top* of the page in *points*. Accepts single integer. e.g 200
        :param page: Number of page, e.g. 4
        :return:
        """
        pass

    def get_item(self, left, top, page, type='any'):
        """Get any item from the PDF (TODO)

        :param left: Distance from the *left* of the page in *points*. Accepts single integer. e.g. 150
        :param top: Distance from the *top* of the page in *points*. Accepts single integer. e.g 200
        :param page: Number of page, e.g. 4
        :param type: Type of the the item.
        :return:
        """
        request_json = {
            'id': int(self.id),
            'page': int(page),
            'type': type,
            'top': int(top),
            'left': int(left)
        }
        _, response = self.__client.send_get(uri='find_content/', data=request_json)
        return response.values()[0]

    def get_metadata(self):
        pass


class APIClient:
    """Main API client class"""

    def __init__(self, token):
        self.client = APIRequest(token=token)

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
