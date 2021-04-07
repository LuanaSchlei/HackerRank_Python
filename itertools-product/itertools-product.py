#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/itertools-product/problem
#
# Title: itertools.product
#


from itertools import product

A = map(int, input().split())
B = map(int, input().split())

cartesiano = list(product(A, B))
cartesiano_string = str(cartesiano)
cartesiano_sem_colchetes = cartesiano_string.replace('[', '').replace(']','')
cartesiano_sem_virgula = cartesiano_sem_colchetes.replace('), (', ') (')
print(cartesiano_sem_virgula)