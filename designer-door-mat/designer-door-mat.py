

traco = '-'
meio = '.|.'
welcome = 'WELCOME'

#n, m = map(int, input().split())
num_linhas, num_colunas = 7, 21

#print(n)
#print(m)

for linha in range(num_linhas//2):
    saida = meio * (linha*2+1)
    tamannho_tracos = (num_colunas - len(saida)) // 2
    bloco_tracos = traco * tamannho_tracos
    saida = bloco_tracos + saida + bloco_tracos
    print(saida)

tamanho_welcome = len(welcome)
quantidade_tracos = ( num_colunas - tamanho_welcome ) // 2
saida_welcome = (quantidade_tracos * traco) + welcome + (quantidade_tracos * traco)
print(saida_welcome) 

for linha in range(num_linhas//2, 0,-1):
    saida = meio * (linha*2-1)
    tamannho_tracos = (num_colunas - len(saida)) // 2
    bloco_tracos = traco * tamannho_tracos
    saida = bloco_tracos + saida + bloco_tracos
    print(saida)


#    if caracter == n:
#        parte1 = risco * caracter
#        parte1_zip = zip(parte1)
#        parte2 = risco * m
#        parte3 = welcome.ljust(m)
#   print(parte1 + parte2 + parte3)

#
# for caracter in range(n, m + 1):
# a quantidade de linhas sera determinado pelo valor de n
# o comprimento das linhas serao determinados pelo valor de m.
#
# primeira linha:
# a primeira linha sera preenchido por riscos,
# sendo que 3 desses riscos terao que ser substituidos no centro da linha por 
# 1*(1 ponto, 1 barra e 1 ponto), nessa ordem.
# entao a quantidade de riscos será determinada pelo valor de m-3.

