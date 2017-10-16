import os
from behave import given, then


@given('the pdf file "{pdf_path}" is sent to be analized')
def create_job_analysis_step(context, pdf_path):
    full_pdf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), pdf_path)
    client = context.config.userdata['client']

    job = client.create_job(local_file=full_pdf_path, wait_to_complete=True)
    context.config.userdata['job'] = job


@then('I can read the text')
def verify_text_from_pdf_step(context):
    pass
