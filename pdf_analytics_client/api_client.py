#!/usr/bin/env python
"""
PDFAnalytics API Client

A high level module that enables the submission of the test cases and the
test results to the MatrixMedicalRequirements.

It uploads both the test results and the test description at tht same time.
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
        """Wait for the PDF analysis to complete max 20 secs"""
        count = 0
        while self.get_status() == 'In Progress' and count < 10:
            time.sleep(3)
            count += 1

        final_status = self.get_status()
        if final_status == 'In Progress':
            raise Exception('The job was not processed in 20 seconds')
        else:
            return

    def get_status(self):
        _, response = self.__client.send_get(uri='job/{id}/get_status/'.format(id=self.id))
        return response['status']

    def verify_image(self, local_file, left, top, page):
        request_json = {
            'id': int(self.id),
            'page': int(page),
            'top': int(top),
            'left': int(left)
        }
        file_name = os.path.basename(local_file)
        files = {'image_file': (file_name, open(local_file, 'rb'))}
        status_code, response = self.__client.send_post(uri='job/verify_image/', data=request_json, ofile=files)

        if status_code != 200:
            raise Exception(response)

        print(response)
        return response

    def verify_text(self):
        pass

    def get_item(self, left, top, page, type='any'):
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

    def create_job(self, local_file, wait_to_complete=False):
        """Create a PDF analysis job

        :param local_file: the path of the local PDF file that needs to be uploaded to the server for the analysis
        :param wait_to_complete: wait for the PDF analysis to complete
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
