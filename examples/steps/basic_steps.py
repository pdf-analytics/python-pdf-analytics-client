import os
from behave import given, then


@given('the pdf file "{pdf_path}" is sent to be analysed')
def create_job_analysis_step(context, pdf_path):
    # Get the full pdf path
    full_path = os.path.join(context.project_dir, pdf_path)

    # Create a new job analysis
    client = context.config.userdata['client']
    job = client.create_job(local_file=full_path, wait_to_complete=True)
    context.config.userdata['job'] = job


@then('I read "{text}", at [left, top] ["{left}", "{top}"] on page "{page}" in pdf')
def verify_text_from_pdf_step(context, text, left, top, page):
    job = context.config.userdata['job']
    item = job.get_item(left=left, top=top, page=page)
    assert text in item['text'], "Comparing: {actual}, {expected}".format(actual=text,expected=item['text'])


@then('I check font of the text at [left, top] ["{left}", "{top}"] on page "{page}" in pdf, is "{font}"')
def verify_text_from_pdf_step(context, left, top, page, font):
    job = context.config.userdata['job']
    item = job.get_item(left=left, top=top, page=page)
    assert font in item['font'], "Comparing: {actual}, {expected}".format(actual=font,expected=item['font'])


@then('I see the image "{img_filename}", at [left, top] ["{left}", "{top}"] on page "{page}" in pdf')
def verify_text_from_pdf_step(context, img_filename, left, top, page):
    job = context.config.userdata['job']
    img_path = os.path.join(context.project_dir, img_filename)
    job.verify_image(local_file=img_path, left=left, top=top, page=page)
    #assert text in item['text'], "Comparing: {actual}, {expected}".format(actual=text,expected=item['text'])
