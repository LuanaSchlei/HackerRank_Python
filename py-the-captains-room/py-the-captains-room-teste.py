#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-the-captains-room/problem
#
# Title: The Captain's Room
#
# Arquivo de Teste
#

from collections import Counter

# size_each_group = int(input())
input_size_each_group = '5'
size_each_group = int(input_size_each_group)
print(size_each_group)

# elements_rooms_number = list(map(int, input().split()))
input_elements_rooms_number = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 '
elements_rooms_number_split = list(map(int, input_elements_rooms_number.split()))
print(elements_rooms_number_split)

elements_rooms_number_counter = Counter(elements_rooms_number_split)
print(elements_rooms_number_counter)

for i in elements_rooms_number_counter:
    # print(i)
    if elements_rooms_number_counter[i] == 1:
        print(i)
        
        
