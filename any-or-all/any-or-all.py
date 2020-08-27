#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/any-or-all/problem
#
# Title: Any or All
#

number_integer = int(input())
input_list = input()
list_split = map(int, input_list.split())

l_aux = map(lambda x: x > 0, list_split)
p_aux = map(lambda x: x == x[::-1], input_list.split())

print(all(l_aux) and any(p_aux))