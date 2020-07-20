#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/capitalize/problem
#
# Title: Capitalize
#

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    saida = ''
    procurando_letra = True
    for letra in s:
        if procurando_letra:
            if letra != ' ':
                saida += letra.upper()
                procurando_letra = False
            else:
                saida += letra
        else:
            if letra == ' ':    
                procurando_letra = True
                saida += letra
            else:
                saida += letra


    return saida

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
