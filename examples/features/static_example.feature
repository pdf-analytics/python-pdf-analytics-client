Feature: Verify PDF content on run
    As a user, I need to check the PDF content on the run
    So that I

    Scenario: Verify textural content
        Given the pdf file "demo_file.pdf" is sent to be analysed
        Then I read "This is a demo PDF file", at [left, top] ["118", "65"] on page "1" in pdf
        And I check font of the text at [left, top] ["118", "65"] on page "1" in pdf, is "LiberationSerif, 15.41"
        And I read "Text at the top of the second page.", at [left, top] ["147", "65"] on page "2" in pdf
        And I see the image "apple.png", at [left, top] ["300", "250"] on page "1" in pdf
        And I see the image "apple_diff.png", at [left, top] ["300", "250"] on page "1" in pdf
        And I check the metadata key "Creator" that is "Writer"
        And I check the metadata key "Producer" that is "LibreOffice 4.3"

    Scenario: Verify textural content
        Given the pdf file "demo_file.pdf" is sent to be analysed
        Then I compare the "demo_file.pdf" with the uploaded pdf



        # signed
        #try different font size
        # PDF to PDF comparison
        # text on every page e.g. 3-5, all, last, 2,5
