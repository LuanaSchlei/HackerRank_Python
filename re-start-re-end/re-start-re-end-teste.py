#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/re-start-re-end/problem
#
# Title: Re.start() & Re.end()
#
# Arquivo de Teste
#

import re

s = 'jjhv'
k = 'z'
pattern = re.compile(k)
m = pattern.search(s)
#print(m)
if not m:
    print('({0}, {1})'.format(-1, -1))
while m:
    print('({0}, {1})'.format(m.start(), m.end() - 1))
    m = pattern.search(s, m.start() + 1)
