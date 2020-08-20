#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-mod-divmod/problem
#
# Title: Mod Divmod
#
# Arquivo de Teste
#

# input_a = int(input())
input_a = '177'
int_a = int(input_a)

# input_b = int(input())
input_b = '10'
int_b = int(input_b)

division_a_b = int_a // int_b 
print(division_a_b)

modul_a_b = int_a % int_b
print(modul_a_b)

divmod_a_b = divmod(int_a, int_b)
print(divmod_a_b)