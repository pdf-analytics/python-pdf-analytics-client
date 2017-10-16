Feature: Create and analysis PDF

    Scenario: Create a PDF analysis
        Given the pdf file "demo_file.pdf" is sent to be analysed
        Then I verify see the text "This is a demo PDF file" at the pdf, at left "118", top "65", page "1"
