#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
#
# Title: Set .discard(), .remove() & .pop()
#


input_num_elements = int(input())
#input_num_elements = '9'
#num_int = int(input_num_elements)
# print(input_num_elements)

# input_n_elements = '1 2 3 4 5 6 7 8 9'
input_n_elements_set = set(map(int, input().split()))
# input_n_elements_set = set(map(int, input_n_elements.split()))
# print(input_n_elements_set)

input_num_comandos = int(input())
# input_num_comandos = '10'
# num_comandos_int = int(input_num_comandos)
# print(input_num_comandos)

# input_comandos = ['pop',
#                  'remove 9',
#                  'discard 9',
#                  'discard 8',
#                  'remove 7',
#                  'pop',
#                  'discard 6',
#                  'remove 5',
#                  'pop',
#                  'discard 5']

for i in range(input_num_comandos):
    comand_line = input()
    # comand_line = input_comandos[i]
    # print(comand_line)
    comand_line_split = comand_line.split()
    # print(comand_line_split)
    comand = comand_line_split[0]
    if comand == 'pop':
        input_n_elements_set.pop()
    elif comand == 'remove':
        parametro = int(comand_line_split[1])
        input_n_elements_set.remove(parametro)
    elif comand == 'discard':
        parametro = int(comand_line_split[1])
        input_n_elements_set.discard(parametro)
print(sum(input_n_elements_set))
