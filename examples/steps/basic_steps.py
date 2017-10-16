import os
from behave import given, then


@given('the pdf file "{pdf_path}" is sent to be analysed')
def create_job_analysis_step(context, pdf_path):
    # Get the full pdf path
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(dir_path, pdf_path)

    # Create a new job analysis
    client = context.config.userdata['client']
    job = client.create_job(local_file=full_path, wait_to_complete=True)
    context.config.userdata['job'] = job


@then('I can read the text')
def verify_text_from_pdf_step(context):
    pass
