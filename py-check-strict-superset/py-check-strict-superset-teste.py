#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
#
# Title: Check Strict Superset
#
# Arquivo de Teste
#

# input_elements_a = set(map(int, input().split()))
input_elements_a = '1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78'
elements_a = set(map(int, input_elements_a.split()))

# number_sets = int(input())
input_number_other_sets = '2'
number_sets = int(input_number_other_sets)

input_sets = ['1 2 3 4 5',
              '100 11 12']

is_superset_for_all = True
for i in range(number_sets):
    # set_b = set(map(int, input().split()))
    set_b = set(map(int, input_sets[i].split()))
    if not elements_a.issuperset(set_b):
        is_superset_for_all = False
        break
print(is_superset_for_all)