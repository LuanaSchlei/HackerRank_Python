#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-add/problem
#
# Title: Set .add()
#

int_total_de_selos = int(input())
# total_de_selos = '7'
# int_total_de_selos = int(total_de_selos)
# print(int_total_de_selos)
# selos = 'UK, China, USA, France, New Zeland, UK, France'
# selos_split = selos.split(', ')
# print(selos_split)
selos_sem_duplicatas = set()

for i in range(int_total_de_selos):
    input_selos = input()
    # input_selos = selos_split[i]
    selos_sem_duplicatas.add(input_selos)

print(len(selos_sem_duplicatas))