from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pdf_analytics_client import APIClient


def before_all(context):
    """Setup to create a session with the PDFAnalytics cloud"""
    if context.config.userdata.get('url', False):
        context.config.userdata['client'] = APIClient(token=context.config.userdata['token'],
                                                      url=context.config.userdata['url'])
    else:
        context.config.userdata['client'] = APIClient(token=context.config.userdata['token'])

    context.project_dir = os.path.dirname(os.path.abspath(__file__))


def before_scenario(context, scenario):
    scenario.continue_after_failed_step = True