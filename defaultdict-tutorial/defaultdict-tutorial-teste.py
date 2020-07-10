#
# Url: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
#
# Title: DefaultDict Tutorial
#
# Arquivo de Teste

from collections import defaultdict

# n, m = map(int, input().split(' '))
n, m = 5, 2
# print(n, m)
# Listas que serao usadas para simular o 'n' e o 'm'.
a_list = ['a', 'a', 'b', 'a', 'b']
b_list = ['a', 'b']

d2 = defaultdict(list)
for indice in range(n):
#   valor = input()
    valor = a_list[indice]
    d2[valor].append(indice + 1)
#    print(d2)
        
for indice in range(m):
#   valor = input()
    palavra_m = b_list[indice]
    if palavra_m in d2:
        resposta = d2[palavra_m]
#        print(resposta)
        resposta_string = ' '.join(map(str, resposta))
        print(resposta_string)
    else:
        print(-1)
















