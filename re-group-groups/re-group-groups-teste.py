#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/re-group-groups/problem
#
# Title: Group(), Groups() & Groupdict()
#
# Arquivo de Teste
#

import re

# input_s = input()
input_s = '..123AA4567890111213141516171820212223'
# input_s = '..123'
s = re.search(r'([a-zA-Z0-9])\1+', input_s)
# print(s)
if s is None:
    print(-1)
else:
    print(s.group(1))

    


