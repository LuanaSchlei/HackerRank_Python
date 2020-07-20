#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
#
# Title: Introduction to Sets
#



def average(array):

    alturas_distintas_set = set(array)
    alturas_distintas_len = len(alturas_distintas_set)
    soma_alturas_distintas = sum(alturas_distintas_set)
    media_alturas_distintas = soma_alturas_distintas / alturas_distintas_len

    return media_alturas_distintas

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)