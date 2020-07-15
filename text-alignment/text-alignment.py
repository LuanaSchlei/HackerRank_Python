

#Replace all ______ with rjust, ljust or center. 

#thickness = int(input()) #This must be an odd number
thickness = 21
num_linhas = 7
c = '.|.'
w = 'WELCOME'
comprimento_welcome = len(w)
linhas_antes_welcome = num_linhas // 2
traco = '-'
quantidade_caracteres_para_centralizar = (thickness - len(c)) // 2

#Top Cone
for linha in range(linhas_antes_welcome):
    lado_direito = ((c*linha).rjust(quantidade_caracteres_para_centralizar, '-'))
    lado_esquerdo = ((c*linha).ljust(quantidade_caracteres_para_centralizar, '-'))
    saida = lado_direito + c + lado_esquerdo
    print(saida)
    center_saida = (c*(linha*2+1)).center(21, '-')
    print(center_saida)
    print(' ')
#Top Pillars
#for linha in range(num_linhas+1):
#   lado_direito = ((c*linha).rjust(thickness-1, '-'))
#   lado_esquerdo = ((c*linha).ljust(thickness-1, '-'))
#   tamanho_welcome = len(w)
#   saida = lado_direito + w+ lado_esquerdo
#   print(saida)

#Middle Belt

quantidade_tracos = ( thickness - comprimento_welcome ) // 2
saida_welcome = (quantidade_tracos * traco) + w + (quantidade_tracos * traco)
central_welcome = (w.center(thickness, '-')) 
print(central_welcome)    

#Bottom Pillars
#for i in range(thickness+1):
#    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
#for i in range(thickness):
#    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


for linha in range(linhas_antes_welcome, 0, -1):
    lado_direito = ((c*(linha-1)).rjust(quantidade_caracteres_para_centralizar, '-'))
    lado_esquerdo = ((c*(linha-1)).ljust(quantidade_caracteres_para_centralizar, '-'))
    saida = lado_direito + c + lado_esquerdo
    print(saida)
    center_saida = (c*(linha*2-1)).center(21, '-')
    print(center_saida)
    print(' ')


