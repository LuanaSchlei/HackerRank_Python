#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-check-subset/problem
#
# Title: Check Subset
#
# Arquivo de Teste
#

# number_tests_cases = int(input())
input_number_tests = '3'
number_tests_cases = int(input_number_tests)
# print(number_tests_cases)


input_lines = ['5',
               '1 2 3 5 6',
               '9',
               '9 8 5 6 3 2 1 4 7',
               '1',
               '2',
               '5',
               '3 6 5 4 1',
               '7',
               '1 2 3 5 6 8 9',
               '3',
               '9 8 2']

index_line = 0

for i in range(number_tests_cases):
    # number_elements_a = int(input())
    number_elements_a = input_lines[index_line]
    index_line += 1
    # print(number_elements_a)

    # elements_set_a = set(map(int, input().split()))
    elements_set_a = set(map(int, input_lines[index_line].split()))
    index_line += 1 
    # print(elements_set_a)

    # number_elements_b = int(input())
    number_elements_b = input_lines[index_line]
    index_line += 1
    # print(number_elements_b)

    # elements_set_b = set(map(int, input().split()))
    elements_set_b = set(map(int, input_lines[index_line].split()))
    index_line += 1 
    # print(elements_set_b)

    print(elements_set_a.issubset(elements_set_b))

