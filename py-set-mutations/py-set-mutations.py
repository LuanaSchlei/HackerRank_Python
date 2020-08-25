#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-mutations/problem
#
# Title: Set Mutations
#

input_num_elements_a = int(input())
n_elements_set = set(map(int, input().split()))
input_num_sets = int(input())
input_comand_index = 0

for i in range(input_num_sets):
    comand_line = input()
    input_comand_index += 1
    set_for_comand_line = set(map(int, input().split()))
    input_comand_index += 1 
    comand_line_split = comand_line.split()
    comand = comand_line_split[0]
    if comand == 'intersection_update':
        n_elements_set.intersection_update(set_for_comand_line)
    if comand == 'update':
        n_elements_set.update(set_for_comand_line)
    if comand == 'symmetric_difference_update':
        n_elements_set.symmetric_difference_update(set_for_comand_line)
    if comand == 'difference_update':
        n_elements_set.difference_update(set_for_comand_line)
print(sum(n_elements_set))
