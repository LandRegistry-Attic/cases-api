#!/bin/bash

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"

rvm use ruby-1.9.3-p551

set -e

rm -rf diff2*
rm -rf tmpimg*
rm -rf sshot*

bundle install

if [ -z "$1" ]
 then
   cucumber --tags ~@wip --tags ~@removed --format json --out report.json --format pretty
else
   cucumber -r features $1
fi

rvm use jruby-1.7.19
