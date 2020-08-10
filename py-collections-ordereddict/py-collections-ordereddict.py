#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
#
# Title: Collections.ordereddict()
#

from collections import OrderedDict

numero_itens = numero_itens = int(input())

compra = OrderedDict()

for i in range(numero_itens):
    item = input()
    item_lista = item.split()
    valor_lista = item_lista[-1:]
    valor_item = int(item_lista[-1:][0])
    leng_preco = len(item_lista[-1:][0])
    leng_preco_aux = leng_preco * -1
    nome_item = item[:leng_preco_aux].strip()
    if nome_item in compra:
        compra[nome_item] = compra[nome_item] + valor_item
    else:
        compra[nome_item] = valor_item

for i in compra:
    print(i, compra[i])

