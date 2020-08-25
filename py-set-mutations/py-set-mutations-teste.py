#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-mutations/problem
#
# Title: Set Mutations
#
# Arquivo de Teste
#

# input_num_elements_a = int(input())
input_num_elements_a = '16'
num_elem_a_int = int(input_num_elements_a)
print(num_elem_a_int)

# n_elements_set = set(map(int, input().split()))
input_elements = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52'
n_elements_set = set(map(int, input_elements.split()))
print(n_elements_set)

# input_num_sets = int(input())
input_num_sets = '4'
num_sets_int = int(input_num_sets)
print(num_sets_int)

input_comandos = [' intersection_update 10',
                  '2 3 5 6 8 9 1 4 7 11',
                  'update 2',
                  '55 66',
                  'symmetric_difference_update 5',
                  '22 7 35 62 58',
                  'difference_update 7',
                  '11 22 35 55 58 62 66']

input_comand_index = 0

for i in range(num_sets_int):
    # comand_line = input()
    comand_line = input_comandos[input_comand_index]
    input_comand_index += 1
    print(comand_line)
    # set_for_comand_line = set(map(int, input().split()))
    set_for_comand_line = set(map(int,input_comandos[input_comand_index].split()))
    input_comand_index += 1 
    print(set_for_comand_line)
    comand_line_split = comand_line.split()
    print(comand_line_split)
    comand = comand_line_split[0]
    print(comand)
    if comand == 'intersection_update':
        n_elements_set.intersection_update(set_for_comand_line)
    if comand == 'update':
        n_elements_set.update(set_for_comand_line)
    if comand == 'symmetric_difference_update':
        n_elements_set.symmetric_difference_update(set_for_comand_line)
    if comand == 'difference_update':
        n_elements_set.difference_update(set_for_comand_line)
print(sum(n_elements_set))
