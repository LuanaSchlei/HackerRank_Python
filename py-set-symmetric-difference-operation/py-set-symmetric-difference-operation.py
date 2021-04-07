#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
#
# Title: Set .symmetric_difference() Operation
#

input_n_subscribed_english = int(input())
input_n_roll_students_english = input()
n_roll_students_english_split = input_n_roll_students_english.split()
n_roll_students_english_set = set(n_roll_students_english_split)

input_n_subscribed_french = int(input())
input_n_roll_students_french = input()
n_roll_students_french_split = input_n_roll_students_french.split()
n_roll_students_french_set = set(n_roll_students_french_split)

set_symmetric_difference = n_roll_students_english_set.symmetric_difference(n_roll_students_french_set)
result = len(set_symmetric_difference)
print(result)