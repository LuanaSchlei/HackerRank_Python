#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/input/problem
#
# Title: Input()
#

x_s, k_s = input().split()
x = int(x_s)
k = int(k_s)

p = input()
r = eval(p)

print(r == k)