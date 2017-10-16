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


@then('I verify see the text "{text}" at the pdf, at left "{left}", top "{top}", page "{page}"')
def verify_text_from_pdf_step(context, text, left, top, page):

    job = context.config.userdata['job']
    item = job.get_item(left=left, top=top, page=page)
    print(item)
    assert text in item[0]['text']
