#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/introduction-to-regex/problem
#
# Title: Detect Floating Point Number
#

number_tests_cases = int(input())

for i in range(number_tests_cases):
    tests_cases = input()
    try:
        if '.' in tests_cases:
            cases_float = float(tests_cases)
            print(True)
        else:
            print(False)
    except ValueError as detail:
        print(False)