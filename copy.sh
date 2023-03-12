#!/usr/bin/env bash
# fail if any commands fails
set -e
# debug log
set -x

# write your script here
cp ktlint-report.xml /Users/tedomanvelidze/StudioProjects/Dangerplayground/build/reports/ktlint/ktlint-report.xml

cp lint-report.xml /Users/tedomanvelidze/StudioProjects/Dangerplayground/build/reports/lint/lint-report.xml

less /Users/tedomanvelidze/StudioProjects/Dangerplayground/build/reports/ktlint/ktlint-report.xml
less /Users/tedomanvelidze/StudioProjects/Dangerplayground/build/reports/lint/lint-report.xml