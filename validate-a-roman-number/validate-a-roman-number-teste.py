#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/validate-a-roman-number/problem
#
# Title: Validating Roman Numerals
#
# Arquivo de Teste
#

import re

# input_num_roman = input()
# input_upper_case = input_num_roman.upper()
input_num_roman = 'CDXxi'
input_upper_case = input_num_roman.upper()

thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"
regex = thousand + hundred + ten + unit
print(regex)
regex_pattern = r"^" + regex + "$"
print(regex_pattern)
result = str(bool(re.match(regex_pattern, input_upper_case)))
print(result)
