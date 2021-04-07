#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-if-else/problem
#
# Title: Python If-Else
#
# Arquivo de Teste
#

import math
import os
import random
import re
import sys


if __name__ == '__main__':
#    n = int(input().strip())
    n = 3
    if n % 2 != 0:
        print('Weird')
    elif 2 <= n < 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')

   