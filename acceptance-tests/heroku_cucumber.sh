#!/bin/bash

set -e

rm -rf diff2*
rm -rf tmpimg*
rm -rf sshot*

bundle install

export ENVIRONMENT="preview"

cucumber --tags ~@wip --tags ~@removed --tags ~@performance_test --format json --out report.json --format pretty
