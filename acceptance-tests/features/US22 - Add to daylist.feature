Feature: US22 - Add new case to daylist
As a customer I need Land Registry to be able to accept my application So that I can protect my interests


Acceptance Criteria
add correct data to end of database list in time and date order - borower name, lender name, mortgage date, property details, title number, md ref, key number, applicant details, applicant reference, amount paid



Scenario: Submitting a new case for display at bottom of daylist

Given that a new case has been submitted
And a unique reference is generated
When I view the daylist
Then I see the new case on the daylist
And the cases are ordered by date and time
