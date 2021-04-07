#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
#
# Title: Alphabet Rangoli
#
# Arquivo de Teste
#

import string

alfabeto = string.ascii_lowercase

traco = '-'


def print_rangoli(size):
    if size == 1:
        print('a')
        return
    letras = size + (size - 1) # -1 pq o 'a' nao repete, size correponde a quantidade de letras
    traco = letras - 1   # -1 pq apos a  ultima letra nao vai traco
    colunas = letras + traco
    alfabeto_local = alfabeto[:size]
    alfabeto_revertido = list(alfabeto_local)
    alfabeto_revertido.reverse()
    letras_anteriores = []
    for letra_atual in alfabeto_revertido:
        texto_meio = '-'.join(letras_anteriores) + '-' + letra_atual + '-'
        letras_anteriores.reverse()
        texto_meio += '-'.join(letras_anteriores)
        letras_anteriores.reverse()
        linha = texto_meio.center(colunas, '-')
        print(linha)
        letras_anteriores.append(letra_atual)

    if size > 1: 
        alfabeto_local = alfabeto[1:size]
        letras_anteriores.pop()    # remove o 'a'
        letras_anteriores.pop()    # remove o 'b'
        for letra_atual in alfabeto_local:
            texto_meio = '-'.join(letras_anteriores) + '-' + letra_atual + '-'
            letras_anteriores.reverse()
            texto_meio += '-'.join(letras_anteriores)
            letras_anteriores.reverse()
            linha = texto_meio.center(colunas, '-')
            print(linha)
            if letras_anteriores:
                letras_anteriores.pop()

if __name__ == '__main__':
    n = 2
    print_rangoli(n)
