#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/itertools-permutations/problem
#
# Title: itertools.permutations
#

from itertools import permutations

#  s = ('HACK', 2)

#def junta_letras(tupla):
#    return ''.join(tupla)



s, k = 'HACK 2'.split(' ')
comprimento_s = len(s)
ki = int(k)

permutacao = list(permutations(s, ki))
#print(permutacao)

# mapea cada elemento da lista em uma string
s_itens_juntos = list(map(lambda x: ''.join(x), permutacao))

# ele coloca em ordem alfabetica
s_itens_juntos.sort()

# junta os itens, imprmindo em cada linda usando \n
saida = '\n'.join(s_itens_juntos)
print(saida)

#s_itens_juntos2 = list(map(lambda x: len(x), permutacao))
#s_itens_juntos3 = list(map(lambda x: print(x), permutacao))
#s_itens_juntos4 = list(map(junta_letras, permutacao))


#print(s_itens_juntos2)
#print(s_itens_juntos3)
#print(s_itens_juntos4)