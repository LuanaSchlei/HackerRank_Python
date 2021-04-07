#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-print/problem
#
# Title: Print Function
#


if __name__ == '__main__':
    n = int(input())

    string = ''
    for s in range(1, n + 1):
        string += str(s)
    print(string)