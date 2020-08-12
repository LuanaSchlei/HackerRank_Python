#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/itertools-combinations/problem
#
# Title: itertools.combinations()
#

from itertools import combinations

input_s_k = input()
s_split = input_s_k.split()
s_value = s_split[0]
s_upper = s_value.upper()
s_list = list(s_upper)
s_sorted = sorted(s_list)
s_letra_por_linha = '\n'.join(map(lambda x: str(x), s_sorted))
# print(s_letra_por_linha)

k_value = s_split[1]
k_int = int(k_value)

for i in range(k_int):
    s_letra_por_linha = ''.join(map(str, s_sorted))
    # print(s_letra_por_linha)
    s_lista = list(combinations(s_sorted, i+1))
    # print(s_lista)
    s_combi = list(map(lambda x: ''.join(x), s_lista))
    # print(s_combi)
    s_result = '\n'.join(s_combi)
    print(s_result)
