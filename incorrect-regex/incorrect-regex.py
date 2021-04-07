#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/incorrect-regex/problem
#
# Title: Incorrect Regex
#

import re

number_of_tests = int(input())

for teste in range(number_of_tests):
    input_s = input()
    # input_s = input_valores[teste]
    try:
        aux = re.compile(input_s)
        print(True)
    except Exception as e:
        print(False)