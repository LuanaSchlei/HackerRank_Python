#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/introduction-to-regex/problem
#
# Title: Detect Floating Point Number
#
# Arquivo de Teste
#


# number_tests_cases = int(input())
number_tests_cases = '5'
number_tests_cases_int = int(number_tests_cases)
print(number_tests_cases_int)

tests_cases2 = ['4.0O0',
                '-1.00',
                '+4.54',
                'SomeRandomStuff']

tests_cases = ['1.414',
               '+.5486468',
               '0.5.0',
               '1+1.0',
               '0']


for i in range(number_tests_cases_int):
    # tests_cases = input()
    print(i)
    cases = tests_cases[i]
    print(cases)
    try:
        if '.' in cases:
            cases_float = float(cases)
            print(True)
        else:
            print(False)
    except ValueError as detail:
        print(False)
