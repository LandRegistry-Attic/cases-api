[![Build Status](https://travis-ci.org/LandRegistry/cases-api.svg?branch=master)](https://travis-ci.org/LandRegistry/cases-api)

[![Coverage Status](https://coveralls.io/repos/LandRegistry/cases-api/badge.svg?branch=unit-tests)](https://coveralls.io/r/LandRegistry/cases-api?branch=unit-tests)

# Cases API

This repo is the API to retrieve a list of cases.

These are the available endpoints:

`/cases` - Returns all available cases

`/cases/<casenumber>` - Returns a specific case

## Data structure

This api has a route "/cases", when posted to will create a new case
and return a unique reference for that case. The api expects the case information
posted to look like this:

{
    "dateReceived": "1993-11-01T12:00:00Z",
    "lender": "Example Lender",
    "mortgageDate": "1993-08-13T12:00:00Z",
    "titleNumber": "DN1"
}

##How to run unit tests in development

```
Vagrant SSH into repo
Type: 
source /vagrant/.venv/cases-api/bin/activate

sudo pip install -r requirements_test.txt

Then to run the tests issue this

py.test --cov application tests/ --cov-report=term --cov-report=html

A htmlcov/ folder will be created at the root of project with a code coverage report.
```

##How to run acceptance tests in development

```
Vagrant SSH into repo
navigate to acceptance test folder in cases-api

Then to run the tests enter either

sh run-tests.sh
./run-tests.sh
```
