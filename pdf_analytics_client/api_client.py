#!/usr/bin/env python
"""
PDFAnalytics API Client

A high level module that enables the submission of the test cases and the
test results to the MatrixMedicalRequirements.

It uploads both the test results and the test description at tht same time.
"""
import os
import time
import json
import logging

from pdf_analytics_client.api_request import APIRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JobClass:
    """Basic PDF analysis Job class """

    def __init__(self, id, client):
        self.id = id
        self.__client = client

    def wait_analysis_to_complete(self):
        """Wait for the PDF analysis to complete max 20 secs"""
        count = 0
        while self.get_status() == 'In Progress' and count < 10:
            time.sleep(2)
            count += 1

        final_status = self.get_status()
        if final_status == 'In Progress':
            raise Exception('The job was not processed in 20 seconds')
        else:
            return

    def get_status(self):
        _, status = self.__client(uri='job/get_status/')
        return status

    def verify_image(self):
        pass

    def verify_text(self):
        pass

    def get_item(self):
        pass

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
        #files = {'file': ('demo_file.pdf', open(local_file, 'rb'), 'application/pdf')}
        with open(local_file, 'rb') as f:
            filename = 'demo_file.pdf'
            files = {'file': f,
                     'blee':'fsdfsd'}

        #opend_file = open(local_file, 'rb')

        #files = {'file':('demo_file.pdf', opend_file, 'application/pdf')}
        #files = {'file': '{path}'.format(path=local_file)}

            _, job_id = self.client.send_post(uri='job/upload/', ofile=files)
        print(job_id )
        job_obj = JobClass(id=job_id['id'], client=self.client)

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
