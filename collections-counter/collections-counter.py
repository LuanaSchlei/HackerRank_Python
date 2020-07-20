#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/collections-counter/problem
#
# Title: Collections Counter
#

from collections import Counter

quantidade_de_sapatos = int(input())
estoque_de_sapatos_lista = map(int, input().split(' '))
quantidade_de_clientes = int(input())
estoque_por_tamanho = Counter(estoque_de_sapatos_lista)
caixa = 0

for numero_cliente in range(quantidade_de_clientes):
    tamanho_sapato, preco = map(int, input().split(' '))
    if tamanho_sapato in estoque_por_tamanho:
        estoque_por_tamanho[tamanho_sapato] -= 1
        caixa += preco 
        if estoque_por_tamanho[tamanho_sapato] == 0:
            del estoque_por_tamanho[tamanho_sapato]
    
print(caixa)