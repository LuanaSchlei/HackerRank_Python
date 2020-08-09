#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
#
# Title: Collections.namedtuple()
#

from collections import namedtuple

numero_estudantes = int(input())
colunas = input().split()
Student = namedtuple('Student', colunas)
soma_marks = 0

for i in range(numero_estudantes):
    linha = input().split()

    student = Student(linha[0], linha[1], linha[2], linha[3])

    soma_marks = soma_marks + int(student.MARKS)

media_marks = soma_marks / int(numero_estudantes)
arredondar_marks = "%.2f" % media_marks
print(arredondar_marks)