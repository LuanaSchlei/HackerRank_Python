#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-check-subset/problem
#
# Title: Check Subset
#

number_tests_cases = int(input())

for i in range(number_tests_cases):
    number_elements_a = int(input())
    elements_set_a = set(map(int, input().split()))
    
    number_elements_b = int(input())
    elements_set_b = set(map(int, input().split()))
    
    print(elements_set_a.issubset(elements_set_b))
