Feature: Get a case from API

Scenario: Get case from api
Given that a case is lodged
When I give a valid get request
Then the case details are returned
