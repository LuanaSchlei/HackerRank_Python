#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
#
# Title: Map and Lambda Function
#

cube = lambda x: pow(x, 3)

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0] 
    fib_list = [0, 1]
    any(map(lambda x: fib_list.append(sum(fib_list[-2:])),
                range(2, n)))
    return fib_list  

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
