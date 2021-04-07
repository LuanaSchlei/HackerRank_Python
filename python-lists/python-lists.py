#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-lists/problem
#
# Title: Lists
#

if __name__ == '__main__':
    n = int(input())
    lista = []
    for i in range(n):
        comando = input()
        if comando.startswith('insert'):
            valores = comando.split()
            indice = int(valores[1])
            valor = int(valores[2])
            lista.insert(indice, valor)
        if comando.startswith('print'):
            print(lista)
        if comando.startswith('remove'):
            valores = comando.split()
            valor = int(valores[1])
            lista.remove(valor)
        if comando.startswith('append'):
            valores = comando.split()
            valor = int(valores[1])
            lista.append(valor)
        if comando.startswith('sort'):
            lista.sort()
        if comando.startswith('pop'):
            lista.pop()
        if comando.startswith('reverse'):
            lista.reverse()
        
    
    

        
            


            
        





