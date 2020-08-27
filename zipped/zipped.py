#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/zipped/problem
#
# Title: Zipped!
#

import statistics

students, subjects = input().split()

lista = []

for i in range(int(subjects)):
    marks_in_subjects = input()
    marks_float = list(map(float, marks_in_subjects.split()))
    lista.append(marks_float)

lista_aux_zip = zip(*lista)

for i in lista_aux_zip:
    average_mean = statistics.mean(i)
    print(average_mean)