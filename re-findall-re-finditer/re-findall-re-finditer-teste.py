#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
#
# Title: Re.findall() & Re.finditer()
#
# Arquivo de Teste
#

import re

input_s = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
consoant = 'qwrtypsdfghjklzxcvbnm'
vogal = 'aeiou'
 
regex = '(?<=[' + consoant +'])([' + vogal + ']{2,})[' + consoant + ']'
match = re.findall(regex, input_s, re.I)
print('\n'.join(match or ['-1']))

print('-------------------------------')

if match:
    print('\n'.join(match))
else:
    print('-1')

print('-------------------------------')

if match is None:
    print('-1')
else:
    print('\n'.join(match))