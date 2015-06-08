Feature: Get a case from API

As a caseworker I need to access dynamic data from a work list So that I can do my work

Acceptance Criteria
data is supplied through dynamic web service

Scenario: Get case from api
Given that a case is lodged
When I give a valid get request
Then the case details are returned
