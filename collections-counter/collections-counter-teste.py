
from collections import Counter


#quantidade_de_sapatos = int(input())
#estoque_de_sapatos_lista = map(int, input().split(' '))
#quantidade_de_clientes = int(input())
quantidade_de_sapatos = 10
estoque_de_sapatos_lista = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
quantidade_de_clientes = 6
estoque_por_tamanho = Counter(estoque_de_sapatos_lista)
caixa = 0
#print(estoque_por_tamanho)

for numero_cliente in range(quantidade_de_clientes):
#    tamanho_sapato, preco = map(int, input().split(' '))
    tamanho_sapato, preco = (6, 55)
    if tamanho_sapato in estoque_por_tamanho:
        estoque_por_tamanho[tamanho_sapato] -= 1
#        print(estoque_por_tamanho)
        caixa += preco 
        if estoque_por_tamanho[tamanho_sapato] == 0:
            del estoque_por_tamanho[tamanho_sapato]
    
print(caixa)



    

# Cliente pediu tamanho x
# atendente foi verificar se tem o tamanho x
#   o tamanho x foi encontrado:
#       a atendente leva o sapato tamanho x 
#       a atendente pega o preco do sapato
#       o dinheiro entra no caixa
#       a atendente atualiza o estoque - 1 tamanho de sapato
#       a cliente vai embora
#   se nao foi achado:
#       proximo cliente
# final do dia verificar a quantidade de dinheiro no caixa
    


    
    



    



#esperado_quant_sapatos = 10
#esperado_tamanhos_dos_sapatos = 2, 3, 4, 5, 6, 8, 7, 6, 5, 18
#esperado_quantidade_de_clientes = 6

