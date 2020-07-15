

import textwrap

def wrap(string, max_width):
    saida = ''
    contador = 0 

    for caracter_atual in string:
        if contador == max_width:
            saida += '\n'
            saida += caracter_atual 
            contador = 0
        else:
            saida += caracter_atual
            contador += 1
    return saida

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)