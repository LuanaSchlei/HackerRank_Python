#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/re-split/problem
#
# Title: Re.split()
#

import re

regex_pattern = r'[.,]+'
print("\n".join(re.split(regex_pattern, input())))
