from __future__ import absolute_import, division, print_function, unicode_literals

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
    expected_text = item['text'].replace('\n', '<br>')
    assert text in expected_text, "Comparing: {actual}, {expected}".format(actual=text, expected=expected_text)


@then('I check font of the text at [left, top] ["{left}", "{top}"] on page "{page}" in pdf, is "{font}"')
def verify_text_from_pdf_step(context, left, top, page, font):
    job = context.config.userdata['job']
    item = job.get_item(left=left, top=top, page=page)
    assert font in item['font'], "Comparing: {actual}, {expected}".format(actual=font,expected=item['font'])


@then('I "{action}" see the image "{img_filename}", at [left, top] ["{left}", "{top}"] on page "{page}" in pdf')
def verify_text_from_pdf_step(context, action, img_filename, left, top, page):
    job = context.config.userdata['job']
    img_path = os.path.join(context.project_dir, img_filename)
    response = job.verify_image(path=img_path, left=left, top=top, page=page)
    if action == 'can':
        assert response['result'] is True, "Comparing the image, message: {message}".format(message=response['message'])
    else:
        assert response['result'] is False, "Comparing the image, message: {message}".format(message=response['message'])


@then('I check the metadata key "{key}" that is "{value}"')
def verify_text_from_pdf_step(context, key, value):
    job = context.config.userdata['job']
    actual_value = job.get_metadata()['metadata'].get(key, None)
    assert value == actual_value, "Comparing: {actual}, {expected}".format(actual=actual_value, expected=value)


@then('I compare the "{pdf_file}" with the uploaded pdf')
def verify_text_from_pdf_step(context, pdf_file):
    job = context.config.userdata['job']
    full_path = os.path.join(context.project_dir, pdf_file)
    response = job.verify_pdf(path=full_path)
    assert response['result'] is True, "Comparing the pdf, message: {message}".format(message=response['message'])

