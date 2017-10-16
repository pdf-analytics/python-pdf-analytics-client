import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pdf_analytics_client import APIClient


def before_all(context):
    """Setup to create a session with the PDFAnalytics cloud"""
    context.config.userdata['client'] = APIClient(token=context.config.userdata['token'])
