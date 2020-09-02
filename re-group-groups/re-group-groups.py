#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/re-group-groups/problem
#
# Title: Group(), Groups() & Groupdict()
#

import re

input_s = input()
s = re.search(r'([a-zA-Z0-9])\1+', input_s)
# print(s)
if s is None:
    print(-1)
else:
    print(s.group(1))