#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
#
# Title: Re.findall() & Re.finditer()
#

import re

input_s = input()
consoant = 'qwrtypsdfghjklzxcvbnm'
vogal = 'aeiou'
 
regex = '(?<=[' + consoant +'])([' + vogal + ']{2,})[' + consoant + ']'
match = re.findall(regex, input_s, re.I)
print('\n'.join(match or ['-1']))