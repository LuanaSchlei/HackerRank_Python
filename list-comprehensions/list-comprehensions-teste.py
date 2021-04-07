#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/list-comprehensions/problem
#
# Title: List Comprehensions
#
# Arquivo de Teste
#


if __name__ == '__main__':
#    x = int(input())
#    y = int(input())
#    z = int(input())
#    n = int(input())

    x = 1
    y = 1
    z = 1
    n = 2

    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range( z + 1) if (( i + j + k)  != n)])
