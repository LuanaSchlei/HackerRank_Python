#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/itertools-product/problem
#
# Title: itertools.product
#
# Arquivo de Teste
#

from itertools import product

#A = [1, 2]
#B = [3, 4]

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
B = [0, 1]

#A = map(int, input().split())
#B = map(int, input().split())

cartesiano = list(product(A, B))
cartesiano_string = str(cartesiano)
cartesiano_sem_colchetes = cartesiano_string.replace('[', '').replace(']','')
cartesiano_sem_virgula = cartesiano_sem_colchetes.replace('), (', ') (')
print(cartesiano_sem_virgula)

esperado = '(0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1) (3, 0) (3, 1) (4, 0) (4, 1) (5, 0) (5, 1) (6, 0) (6, 1) (7, 0) (7, 1) (8, 0) (8, 1) (9, 0) (9, 1) (10, 0) (10, 1) (11, 0) (11, 1) (12, 0) (12, 1) (13, 0) (13, 1) (14, 0) (14, 1) (15, 0) (15, 1) (16, 0) (16, 1) (17, 0) (17, 1) (18, 0) (18, 1) (19, 0) (19, 1)'

if esperado == cartesiano_sem_virgula:
    print('é igual')
else:
    print(cartesiano_sem_virgula)
    print(esperado)