

def mutate_string(string, position, character):
    saida = ''
    for posicao_atual in range(len(string)):
        if posicao_atual == position:
            saida += character
        else:
            saida += string[posicao_atual]
    return saida

def mutate_string2(string, position, character):
    saida = ''
    lista_caracteres_da_string = list(string)
    lista_caracteres_da_string[5] = 'k'
    saida = ''.join(lista_caracteres_da_string)

    return saida

def mutate_string3(string, position, character):
    saida = ''
    caracteres_antes_da_posicao = string[: position]
    caracteres_depois_da_posicao = string[position + 1 :]
    saida = caracteres_antes_da_posicao + character + caracteres_depois_da_posicao

    return saida


if __name__ == '__main__':
    s = 'abracadabra'
    i, c = '5 k'.split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    esperado = 'abrackdabra'
    if esperado == s_new:
        print('Houve substituicao na posicao', int(i),'com o caracter ', c)
    else:
        print('Nao houve substituicao')

    