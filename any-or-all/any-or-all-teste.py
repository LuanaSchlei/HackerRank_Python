#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/any-or-all/problem
#
# Title: Any or All
#
# Arquivo de Teste
#


# number_integer = int(input())
total_number_integer = '5'
n_int = int(total_number_integer)
# print(n_int)

# input_list = int(input())
input_list = '12 9 61 5 14'
list_split = map(int, input_list.split())
# print(list_split)

l_aux = map(lambda x: x > 0, list_split)
print(all(l_aux))

p_aux = map(lambda x: x == x[::-1], input_list.split())
print(p_aux)
print(any(p_aux))
print(all(l_aux) and any(p_aux))
