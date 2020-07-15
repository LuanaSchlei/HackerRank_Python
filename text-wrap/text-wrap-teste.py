



import textwrap

def wrap(string, max_width):
    saida = ''
    contador = 0 

    for caracter_atual in string:
        if contador == max_width:
            saida += '\n'
            saida += caracter_atual 
            contador = 1
        else:
            saida += caracter_atual
            contador += 1
# 
# 
# o max_wiht vai ser o tamanho maximo de cada parágrafo, 
# tem que separar caracteres da string por parágrafo, definido por max_width.
# 
# para cada caracter na string, separar os caracteres usando o valor definido pra max.width.
# se o numero de caracteres for menor ou igual a max_width está certo, caso contrario nao esta certo.
#--------------------------------------------------------
# Pseudo código
# contador recebe zero
# para cada caracter na string, 
#   se contador for igual a max_width entao
#       adiciona o separador de linha no final da saida
#       adiciona caracter no final da saida 
#       contador recebe zero
#   senao 
#       adiciona caracter no final da saida 
#       contador recebe contador + 1
#
#


    return saida

if __name__ == '__main__':
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap(string, max_width)
    print(result)
    esperado1 = 'ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ'
    print(esperado1)