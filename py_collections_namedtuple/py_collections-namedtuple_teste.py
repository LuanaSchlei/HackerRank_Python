#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
#
# Title: py-collections-namedtuple
#
# Arquivo de Teste
#

from collections import namedtuple

input_numero_estudantes = '5'
input_colunas = 'ID         MARKS      NAME       CLASS'
input_linhas = ['1          97         Raymond    7',
                '2          50         Steven     4',
                '3          91         Adrian     9',
                '4          72         Stewart    5         ',
                '5          80         Peter      6']


#numero_estudantes = int(input())
numero_estudantes = int(input_numero_estudantes)
print(numero_estudantes)

#colunas = input().split(' ')
colunas = input_colunas.split()
print(colunas)

Student = namedtuple('Student', colunas)
soma_marks = 0

for i in range(numero_estudantes):
    #linha = input().split(' ')
    linha = input_linhas[i].split()
    print(linha)

    student = Student(linha[0], linha[1], linha[2], linha[3])
    print(student)
    print(student.MARKS)

    soma_marks = soma_marks + int(student.MARKS)
    print(soma_marks)

media_marks = soma_marks / int(input_numero_estudantes)
print(media_marks)

arredondar_marks = "%.2f" % media_marks
print(arredondar_marks)