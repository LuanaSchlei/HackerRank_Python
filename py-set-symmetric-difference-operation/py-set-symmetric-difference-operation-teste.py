#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
#
# Title: Set .symmetric_difference() Operation
#
# Arquivo de Teste
#

# input_n_subscribed_english = int(input())
input_n_subscribed_english = '9'
input_n_subscribed_english_int = int(input_n_subscribed_english)
print(input_n_subscribed_english_int)

# input_n_roll_students_english = input()
input_n_roll_students_english = '1 2 3 4 5 6 7 8 9'
input_n_roll_students_english_split = input_n_roll_students_english.split()
print(input_n_roll_students_english_split)
input_n_roll_students_english_set = set(input_n_roll_students_english_split)
print(input_n_roll_students_english_set)

# input_n_subscribed_french = int(input())
input_n_subscribed_french = '9'
input_n_subscribed_french_int = int(input_n_subscribed_french)
print(input_n_subscribed_french_int)

# input_n_roll_students_french = input()
input_n_roll_students_french = '10 1 2 3 11 21 55 6 8'
input_n_roll_students_french_split = input_n_roll_students_french.split()
print(input_n_roll_students_french_split)
input_n_roll_students_french_set = set(input_n_roll_students_french_split)
print(input_n_roll_students_french_set)

set_symmetric_difference = input_n_roll_students_english_set.symmetric_difference(input_n_roll_students_french_set)
result = len(set_symmetric_difference)
print(result)