#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/itertools-combinations/problem
#
# Title: itertools.combinations()
#
# Arquivo de Teste
#

from itertools import combinations

input_s_k = 'hack 2'
s_split = input_s_k.split()
print(s_split)
s_value = s_split[0]
print(s_value)
s_upper = s_value.upper()
print(s_upper)
s_list = list(s_upper)
print(s_list)
s_sorted = sorted(s_list)
print(s_sorted)
s_letra_por_linha = '\n'.join(map(lambda x: str(x), s_sorted))
print(s_letra_por_linha)

k_value = s_split[1]
print(k_value)
k_int = int(k_value)
print(k_int)

# esse map resultaria no mesmo resultado que ao map da linha 22, se nao fosse pelo join que muda a resposta final.
s_letra_por_linha = ''.join(map(str, s_sorted))
s_lista = list(combinations(s_letra_por_linha, k_int))
print(s_lista)
s_combi = list(map(lambda x: ''.join(x), s_lista))
print(s_combi)

# imprime cada item da lista s_combi numa linha diferente
s_result = '\n'.join(s_combi)
print(s_result)

print('------------------------------------------')

for i in range(k_int):
    s_letra_por_linha = ''.join(map(str, s_sorted))
    # print(s_letra_por_linha)
    s_lista = list(combinations(s_sorted, i+1))
    # print(s_lista)
    s_combi = list(map(lambda x: ''.join(x), s_lista))
    # print(s_combi)
    s_result = '\n'.join(s_combi)
    print(s_result)
