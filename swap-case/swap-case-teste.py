
def swap_case(texto):
    saida = ''
    for caracter_atual in texto:
        if caracter_atual.islower():
            saida += caracter_atual.upper()
        elif caracter_atual.isupper():
            saida += caracter_atual.lower()
        else:
            saida += caracter_atual
    return saida



if __name__ == '__main__':
    entrada1 = 'HackerRank.com presents "Pythonist 2".'
    esperado1 = 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
    teste1 = swap_case(entrada1)
    if esperado1 != teste1:
        print('Valor errado: ', teste1)
    else:
        print('Valor correto: ', teste1)
