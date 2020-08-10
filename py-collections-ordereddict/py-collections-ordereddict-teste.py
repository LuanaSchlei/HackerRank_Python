#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
#
# Title: Collections.ordereddict()
#
# Arquivo de Teste
#

from collections import OrderedDict

input_numero_itens = '9'
input_itens = [
    'BANANA FRIES 12',
    'POTATO CHIPS 30',
    'APPLE JUICE 10',
    'CANDY 5',
    'APPLE JUICE 10',
    'CANDY 5',
    'CANDY 5',
    'CANDY 5',
    'POTATO CHIPS 30']

# numero_itens = int(input())
numero_itens = int(input_numero_itens)

compra = OrderedDict()

for i in range(numero_itens):
    # item = input()
    item = input_itens[i]
    print(item)
    item_lista = item.split()
    print(item_lista)
    valor_lista = item_lista[-1:]
    valor_item = int(item_lista[-1:][0])
    print(valor_item)
    leng_preco = len(item_lista[-1:][0])
    print(leng_preco)
    leng_preco_aux = leng_preco * -1
    print(leng_preco_aux)
    nome_item = item[:leng_preco_aux].strip()
    print(nome_item)
    if nome_item in compra:
        compra[nome_item] = compra[nome_item] + valor_item
    else:
        compra[nome_item] = valor_item

print(compra)

for i in compra:
    print(i, compra[i])