Feature: Verify text and figures on PDF

    Scenario: Verify textural content
        Given the pdf file "demo_file.pdf" is sent to be analysed
        Then I read "This is a demo PDF file", at [left, top] ["118", "65"] on page "1" in pdf
        And I check font of the text at [left, top] ["118", "65"] on page "1" in pdf, is "LiberationSerif, 15.41"
        And I read "Text at the top of the second page.", at [left, top] ["147", "65"] on page "2" in pdf
        And I see the image "education_background.jpg", at [left, top] ["147", "65"] on page "1" in pdf

