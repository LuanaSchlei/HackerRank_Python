#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/introduction-to-regex/problem
#
# Title: Detect Floating Point Number
#

import re

number_tests_cases = int(input())

for i in range(number_tests_cases):
    tests_cases = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', tests_cases)))