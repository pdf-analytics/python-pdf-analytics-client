Feature: Verify payslip PDF content
    As a user, I need to check the PDF content is as expected

    @TC-4
    Scenario: Verify payments and logo @REQ-1, @REQ-3
        Given the pdf file "payslip.pdf" is sent to be analysed
        Then I "can" see the image "payslip_logo.png", at [left, top] ["100", "100"] on page "1" in pdf
        And I read "Total gross <br>payments:", at [left, top] ["74", "599"] on page "1" in pdf
        And I read "£1021.43", at [left, top] ["160", "584"] on page "1" in pdf
        And I read "Total <br>deductions:", at [left, top] ["250", "603"] on page "1" in pdf
        And I read "£304.92", at [left, top] ["334", "587"] on page "1" in pdf
        And I read "Net pay:", at [left, top] ["430", "570"] on page "1" in pdf
        And I read "£716.51", at [left, top] ["516", "586"] on page "1" in pdf

