#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-tuples/problem
#
# Title: Tuples
#

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    h = hash(t)
    print(h)
