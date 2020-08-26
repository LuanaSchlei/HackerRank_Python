#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-the-captains-room/problem
#
# Title: The Captain's Room
#

from collections import Counter

size_each_group = int(input())

elements_rooms_number = list(map(int, input().split()))

elements_rooms_number_counter = Counter(elements_rooms_number)

for i in elements_rooms_number_counter:
    # print(i)
    if elements_rooms_number_counter[i] == 1:
        print(i)