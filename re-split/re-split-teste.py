#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/re-split/problem
#
# Title: Re.split()
#
# Arquivo de Teste
#

import re

# regex_pattern = r'[.,]+'
regex_pattern = r'[\D]+'

s = '100,000,000.000'
s_aux = s.replace(',', '\n').replace('.', '\n')
print(s_aux)

# print("\n".join(re.split(regex_pattern, input())))
print("\n".join(re.split(regex_pattern, s_aux)))
