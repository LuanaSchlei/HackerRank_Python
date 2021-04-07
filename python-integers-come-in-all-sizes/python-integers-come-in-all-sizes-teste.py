#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
#
# Title: Integers Come In All Sizes
#
# Arquivo de Teste
#

# input_a = int(input())
input_a = '9'
int_a = int(input_a)

# input_b = int(input())
input_b = '29'
int_b = int(input_b)

# input_c = int(input())
input_c = '7'
int_c = int(input_c)

# input_d = int(input())
input_d = '27'
int_d = int(input_d)

result = pow(int_a, int_b) + pow(int_c, int_d)
print(result)