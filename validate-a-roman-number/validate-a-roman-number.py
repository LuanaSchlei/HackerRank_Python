#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/validate-a-roman-number/problem
#
# Title: Validating Roman Numerals
#

# regex_pattern = r""	# Do not delete 'r'.

# import re
# print(str(bool(re.match(regex_pattern, input()))))

import re

thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"
regex = thousand + hundred + ten + unit
print(regex)
regex_pattern = r"^" + regex + "$"
print(regex_pattern)
result = str(bool(re.match(regex_pattern, input())))
print(result)