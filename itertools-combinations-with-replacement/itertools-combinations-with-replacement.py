#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
#
# Title: itertools.combinations_with_replacement()
#

from itertools import combinations_with_replacement

input_s_k = input()
split_input = input_s_k.split()

input_s = split_input[0]
s_upper = input_s.upper()
list_s = list(s_upper)
# print(list_s)
s_sorted = sorted(list_s)
# print(s_sorted)
# s_letra_por_linha = '\n'.join(map(lambda x: str(x), s_sorted))
# print(s_letra_por_linha)

input_k = split_input[1]
k_int = int(input_k)

# s_letra_por_linha = ''.join(map(str, s_sorted))
# print(s_letra_por_linha)
s_lista = list(combinations_with_replacement(s_sorted, k_int))
# print(s_lista)
s_combi = list(map(lambda x: ''.join(x), s_lista))
# print(s_combi)
s_result = '\n'.join(s_combi)
print(s_result)