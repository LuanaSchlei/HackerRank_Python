#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
#
# Title: Set .discard(), .remove() & .pop()
#
# Arquivo de Teste
#

# input_num_elements = int(input())
input_num_elements = '9'
num_int = int(input_num_elements)
print(num_int)

input_n_elements = '1 2 3 4 5 6 7 8 9'
# n_elements_set = set(map(int, input().split()))
n_elements_set = set(map(int, input_n_elements.split()))
print(n_elements_set)

# input_num_comandos = int(input())
input_num_comandos = '10'
num_comandos_int = int(input_num_comandos)
print(num_comandos_int)

input_comandos = ['pop',
                  'remove 9',
                  'discard 9',
                  'discard 8',
                  'remove 7',
                  'pop',
                  'discard 6',
                  'remove 5',
                  'pop',
                  'discard 5']

for i in range(num_comandos_int):
    # comand_line = input()
    comand_line = input_comandos[i]
    print(comand_line)
    comand_line_split = comand_line.split()
    print(comand_line_split)
    comand = comand_line_split[0]
    if comand == 'pop':
        n_elements_set.pop()
    elif comand == 'remove':
        parametro = int(comand_line_split[1])
        n_elements_set.remove(parametro)
    elif comand == 'discard':
        parametro = int(comand_line_split[1])
        n_elements_set.discard(parametro)
print(sum(n_elements_set))


