#!/bin/bash

set -e

rm -rf diff2*
rm -rf tmpimg*
rm -rf sshot*

bundle install


export CASES_API_DOMAIN="http://lr-cases-api-alpha.herokuapp.com"

export ENVIRONMENT="preview"

if [ -z "$1" ]
  then
    cucumber --tags ~@wip --tags ~@removed  --tags ~@performance_test --format json --out report.json --format pretty
else
    cucumber -r features $1
fi
