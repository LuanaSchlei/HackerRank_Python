#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
#
# Title: DefaultDict Tutorial
#

from collections import defaultdict

n, m = map(int, input().split(' '))
d = defaultdict(list)

for indice in range(n):
    valor = input()
    d[valor].append(indice + 1)
    
for indice in range(m):
    valor = input()
    if valor in d:
        resposta = d[valor]
        resposta_string = ' '.join(map(str, resposta))
        print(resposta_string)
    else:
        print(-1)





