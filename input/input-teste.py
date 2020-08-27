#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/input/problem
#
# Title: Input()
#
# Arquivo de Teste
#


# x_s, k_s = input().split()
x_s, k_s = '1 4'.split()

x = int(x_s)
k = int(k_s)

# p = input()
p = 'x**3 + x**2 + x + 1 +2'

r = eval(p)
print(r)

print(r == k)

