Feature: US22 - Add new case to daylist
As a customer I need Land Registry to be able to accept my application So that I can protect my interests

As a lender I need to be certain that the title number I have quoted in my application is an existing
live title number
So that I am able to send my application to LR and LR is able to receive the application
and register my interest

Acceptance Criteria
add correct data to end of database list - borrower name, lender name, mortgage date, property details, title number, md ref, key number, applicant details, applicant reference, amount paid

@run_on_DITI_only
Scenario: Add a new case to the daylist

Given I have case information
When a case is submitted
Then an ABR is returned

Scenario: Try to add a case with a closed title number

Given I have case information
And it consists of a closed title number
When a case is submitted
Then a title closed message is returned
# don't forget DL is updated or not
