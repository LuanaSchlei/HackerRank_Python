#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/incorrect-regex/problem
#
# Title: Incorrect Regex
#
# Arquivo de Teste
#

import re

# input_number_of_tests = int(input())
input_number_of_tests = '2'
number_of_tests = int(input_number_of_tests)
input_valores = ['.*\+', '.*+']

for teste in range(number_of_tests):
    input_s = input_valores[teste]
    print(input_s)
    try:
        aux = re.compile(input_s)
        print(True)
    except Exception as e:
        print(False)
    

