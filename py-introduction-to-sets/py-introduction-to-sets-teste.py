#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
#
# Title: Introduction to Sets
#
# Arquivo de teste
#

def average(array):

    alturas_distintas_set = set(array)
    alturas_distintas_len = len(alturas_distintas_set)
    soma_alturas_distintas = sum(alturas_distintas_set)
    media_alturas_distintas = soma_alturas_distintas / alturas_distintas_len

    return media_alturas_distintas

if __name__ == '__main__':
    n = 10
    arr = [161,182,161,154,176,170,167,171,170,174]
    result = average(arr)
    print(result)

    resultado_esperado = 169.375

    if resultado_esperado == result:
        print(f'Está correto o esperado {resultado_esperado} é igual ao result {result}')
    else:
        print(f'Esperado {resultado_esperado} é diferente do resultado {result}')