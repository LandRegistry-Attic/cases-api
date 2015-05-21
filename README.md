[![Build Status](https://travis-ci.org/LandRegistry/cases-api.svg?branch=master)](https://travis-ci.org/LandRegistry/cases-api)

[![Coverage Status](https://coveralls.io/repos/LandRegistry/cases-api/badge.svg?branch=unit-tests)](https://coveralls.io/r/LandRegistry/cases-api?branch=unit-tests)

# Cases API

This repo is the API to retrieve a list of cases.

These are the available endpoints:

`/cases` - Returns all available cases

`/cases/<casenumber>` - Returns a specific case

##How to run unit tests in development

```
Vagrant SSH into repo
navigate to cases-api

run the following commands (until 'workon' is implemented in the environment)

sudo pip install -r requirements.txt
sudo pip install -r requirements_test.txt

Then to run the tests issue this

py.test --cov application tests/ --cov-report=term --cov-report=html

A htmlcov/ folder will be created at the root of project with a code coverage report. 
```
