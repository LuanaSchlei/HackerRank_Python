#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-mod-divmod/problem
#
# Title: Mod Divmod
#

input_a = int(input())
input_b = int(input())

division_a_b = input_a // input_b 
print(division_a_b)

modul_a_b = input_a % input_b
print(modul_a_b)

divmod_a_b = divmod(input_a, input_b)
print(divmod_a_b)