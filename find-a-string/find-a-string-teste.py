#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/find-a-string/problem
#
# Title: Find a string
#
# Arquivo de Teste
#

def count_substring(texto, sub_texto):
    contador = 0
    for indice_atual in range(len(texto)):
        texto_atual = texto[indice_atual:indice_atual + len(sub_texto)]
        if texto_atual == sub_texto:
            contador += 1
    
    return contador

if __name__ == '__main__':
    string = 'ABCDCDC'.strip()
    sub_string = 'CDC'.strip()
    count = count_substring(string, sub_string)
    print(count)
    esperado_count = 2
    if esperado_count == count:
        print('Está correto')
    else:
        print('Está errado:', count)