#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    print(s)
    
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
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1 = 'luana  schlei'
    e1 = 'Luana  Schlei'

    t2 = ' luana silveira e silva schlei'
    e2 = ' Luana Silveira E Silva Schlei'

    result1 = solve(t1)
    result2 = solve(t2)
    if result1 == e1:
        print('Nome capitalizado correto:', result1)
    else:
        print(f'Nome nao foi capitalizado, valor esperado "{e1}", valor retornado "{result1}"')
    if result2 == e2:
        print('Nome capitalizado correto:', result2)
    else:
        print(f'Nome nao foi capitalizado, valor esperado "{e2}", valor retornado "{result2}"')
