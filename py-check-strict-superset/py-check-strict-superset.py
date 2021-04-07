#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
#
# Title: Check Strict Superset
#

elements_a = set(map(int, input().split()))
print(elements_a)

number_sets = int(input())
print(number_sets)

is_superset_for_all = True

for i in range(number_sets):
    set_b = set(map(int, input().split()))
    if not elements_a.issuperset(set_b):
        is_superset_for_all = False
        break
print(is_superset_for_all)