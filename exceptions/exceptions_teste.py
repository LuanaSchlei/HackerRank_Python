#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/exceptions/problem
#
# Title: Exceptions
#
# Arquivo de Teste
#


input_quantidade_de_teste = '3'
input_valores = ['1 0', '2 $', '3 1']

# quantidade_de_teste = int(input())
quantidade_de_teste = int(input_quantidade_de_teste)


for teste in range(quantidade_de_teste):
    # input_test = input().split(' ')
    input_test = input_valores[teste].split(' ')
    try:
        a = int(input_test[0])
        b = int(input_test[1])
        divisao_ab = a//b 
        print(divisao_ab)
    except ZeroDivisionError as detail:
        print('Error Code: integer division or modulo by zero')
    except ValueError as detail:
        print(f'Error Code: {detail}')
    
    