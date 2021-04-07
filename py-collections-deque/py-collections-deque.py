#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-collections-deque/problem
#
# Collections.deque()
#

from collections import deque

d = deque()

input_n_comandos = int(input())
# input_n_comandos = '6'
# input_n_comandos_int = int(input_n_comandos)
# print(input_n_comandos_int)

# input_comandos_parametros = ['append 1',
#                             'append 2',
#                             'append 3',
#                             'appendleft 4',
#                             'pop', 
#                             'popleft']
                            
for i in range(input_n_comandos):
    input_comandos_parametros = input()
    # linha_comando = input_comandos_parametros[i]
    # print(linha_comando)
    input_comandos_parametros_split = input_comandos_parametros.split()
    comando = input_comandos_parametros_split[0]
    if comando == 'append':
        parametro = input_comandos_parametros_split[1]
        d.append(parametro)
    elif comando == 'appendleft':
        parametro = input_comandos_parametros_split[1]
        d.appendleft(parametro)
    elif comando == 'pop':
        d.pop()
    elif comando == 'popleft':
        d.popleft()
print(' '.join(d))
