#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-tuples/problem
#
# Title: Tuples
#
# Arquivo de Teste
#


if __name__ == '__main__':
#    n = int(input())
#    integer_list = map(int, input().split())
    n = 2
    integer_list = (1, 2)
    t = tuple(integer_list)
    h = hash(t)
    print(h)
