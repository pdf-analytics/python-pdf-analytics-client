Feature: Verify PDF content
    As a user, I need to check the PDF content is as expected

    Scenario: Verify textural content
        Given the pdf file "demo_file.pdf" is sent to be analysed
        Then I read "This is a demo PDF file", at [left, top] ["118", "65"] on page "1" in pdf
        And I check font of the text at [left, top] ["118", "65"] on page "1" in pdf, is "LiberationSerif, 15.41"
        And I read "Text at the top of the second page.", at [left, top] ["147", "65"] on page "2" in pdf
        And I check the metadata key "Creator" that is "Writer"
        And I check the metadata key "Producer" that is "LibreOffice 4.3"


    Scenario: Verify figures
        Given the pdf file "demo_file.pdf" is sent to be analysed
        Then I "can" see the image "apple.png", at [left, top] ["300", "250"] on page "1" in pdf
        And I "cannot" see the image "apple_diff.png", at [left, top] ["300", "250"] on page "1" in pdf


    Scenario: Verify PDF with PDF
        Given the pdf file "demo_file.pdf" is sent to be analysed
        Then I compare the "demo_file.pdf" with the uploaded pdf


