#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/symmetric-difference/problem
#
# Title: Symmetric Difference
#

m_input = int(input())
m_integ = input()
num_m = m_integ.split()
num_m_list = list(map(int, num_m))
num_m_set = set(num_m_list)

n_input = int(input())
n_integ = input()
num_n = n_integ.split()
num_n_list = list(map(int, num_n))
num_n_set = set(num_n_list)

m_n_differ = num_m_set.difference(num_n_set)
n_m_differ= num_n_set.difference(num_m_set)
n_m_union = m_n_differ.union(n_m_differ)
n_m_union_sorted = sorted(n_m_union)
n_m_result = '\n'.join(map(str, n_m_union_sorted))
print(n_m_result)