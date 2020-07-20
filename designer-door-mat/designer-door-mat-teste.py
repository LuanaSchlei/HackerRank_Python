#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/designer-door-mat/problem
#
# Title: Designer Door Mat
#
# Arquivo de Teste
#


traco = '-'
meio = '.|.'
welcome = 'WELCOME'

#num_linhas, num_colunas = map(int, input().split())
num_linhas, num_colunas = 7, 21

for linha in range(num_linhas//2):
    saida_meio = meio * (linha*2+1)
    tamannho_tracos = (num_colunas - len(saida_meio)) // 2
    bloco_tracos = traco * tamannho_tracos
    saida_final = bloco_tracos + saida_meio + bloco_tracos
    print(saida_final)

tamanho_welcome = len(welcome)
quantidade_tracos = ( num_colunas - tamanho_welcome ) // 2
saida_welcome = (quantidade_tracos * traco) + welcome + (quantidade_tracos * traco)
print(saida_welcome) 

for linha in range(num_linhas//2, 0,-1):
    saida_meio = meio * (linha*2-1)
    tamannho_tracos = (num_colunas - len(saida_meio)) // 2
    bloco_tracos = traco * tamannho_tracos
    saida_final = bloco_tracos + saida_meio + bloco_tracos
    print(saida_final)
