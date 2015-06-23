Feature: US22 - Add new case to daylist
As a customer I need Land Registry to be able to accept my application So that I can protect my interests

@run_on_DITI_only
Scenario: Add a new case to the daylist

Given I have case information
When a case is submitted
Then an ABR is returned
