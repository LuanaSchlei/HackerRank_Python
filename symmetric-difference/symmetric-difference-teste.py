#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/symmetric-difference/problem
#
# Title: Symmetric Difference
#
# Arquivo de Teste
#

# m = int(input())
input_m = '4'
integ_m = int(input_m)
print(integ_m)

# int_m = int(input())
input_int_m = '2 4 5 9'
num_m = input_int_m.split()
num_m_list = list(map(int, num_m))
num_m_set = set(num_m_list)
print(num_m_set)

# n = int(input())
input_n = '4'
integ_n = int(input_n)
print(integ_n)
# int_n = int(input())

input_int_n = '2 4 11 12'
num_n = input_int_n.split()
num_n_list = list(map(int, num_n))
num_n_set = set(num_n_list)
print(num_n_set)

m_n_differ = num_m_set.difference(num_n_set)
n_m_differ= num_n_set.difference(num_m_set)
n_m_union = m_n_differ.union(n_m_differ)
n_m_union_sorted = sorted(n_m_union)
print(n_m_union_sorted)
n_m_result = '\n'.join(map(str, n_m_union_sorted))
print(n_m_result)

