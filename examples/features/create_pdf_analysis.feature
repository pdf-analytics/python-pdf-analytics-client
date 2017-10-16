Feature: Create and analysis PDF

    Scenario: Create a PDF analysis
        Given the pdf file "demo_file.pdf" is sent to be analized
        Then I can read the text
