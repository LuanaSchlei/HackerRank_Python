#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-set-union/problem
#
# Title: Set .union() Operation
#

input_n_subscribed_english = int(input())
input_n_roll_students_english = input()
n_roll_students_english_split = input_n_roll_students_english.split()
n_roll_students_english_set = set(n_roll_students_english_split)

input_n_subscribed_french = int(input())
input_n_roll_students_french = input()
n_roll_students_french_split = input_n_roll_students_french.split()
n_roll_students_french_set = set(n_roll_students_french_split)

set_union = n_roll_students_english_set.union(n_roll_students_french_set)
result = len(set_union)
print(result)