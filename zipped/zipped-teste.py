#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/zipped/problem
#
# Title: Zipped!
#
# Arquivo de Teste
#

import statistics


# input_students, input_subjects = input().split()
input_students, input_subjects = '5 3'.split()

input_marks_students_in_subjects = ['89 90 78 93 80',
                                    '90 91 85 88 86',
                                    '91 92 83 89 90.5']


lista = []

for i in range(int(input_subjects)):
    # marks_in_sunjects = input()
    marks_in_sunjects = input_marks_students_in_subjects[i]
    # print(marks_in_sunjects)
    # marks_float = list(map(float, marks_in_sunjects.split()))
    marks_float = list(map(float, marks_in_sunjects.split()))
    # print(marks_float)
    lista.append(marks_float)
    # print(lista)

lista_aux_zip = zip(*lista)
# print(lista_aux_zip)

for i in lista_aux_zip:
    # print(i)
    average_mean = statistics.mean(i)
    print(average_mean)