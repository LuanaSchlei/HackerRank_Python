#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#
# Title: Find-second-maximum-number-in-a-list (Find the Runner-Up Score!)
#
# Arquivo de Teste
#





if __name__ == '__main__':
#    n = int(input())
#    arr = map(int, input().split())

    n = 5
    arr = (2, 3, 6, 6, 5)
    
    mx = - 101
    seg_mx = - 101

    for i in arr:

        if i > mx:
            seg_mx = mx
            mx = i
        if i > seg_mx and i < mx:
            seg_mx = i
    print('Segunda pontuacao mais alto:', seg_mx)
            





