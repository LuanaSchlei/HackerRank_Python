#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/zipped/problem
#
# Title: Without Zipped!
#
# Arquivo de Teste
#

# students, subjercts = int(input())
input_students, input_subjects = '5 3'.split()


input_marks_students_in_subjects = ['89 90 78 93 80',
                                    '90 91 85 88 86',
                                    '91 92 83 89 90.5']

sum_marks = []
for i in range(int(input_students)):
    sum_marks.append(0)
    print(sum_marks)

for i in range(int(input_subjects)):
    # input_marks_students_in_subjects = int(input())
    marks_in_sunjects = input_marks_students_in_subjects[i]
    print(marks_in_sunjects)
    marks_float = list(map(float, marks_in_sunjects.split()))
    print(marks_float)
    for i in range(int(input_students)):
        print(marks_float[i])
        sum_marks[i] = sum_marks[i] + marks_float[i]
        print(sum_marks[i])
        media = sum_marks[i] / int(input_subjects)
        print(media)

    
                