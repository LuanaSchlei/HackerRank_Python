


def split_and_join(line):
    saida = ''
    line_split = line.split(' ')
    saida = '-'.join(line_split)
    return saida

if __name__ == '__main__':
    entrada1 = "this is a string"
    esperado1 = 'this-is-a-string'
    teste_1 = split_and_join(entrada1)
    if esperado1 != teste_1:
        print('Valor errado: ', teste_1)
    else:
        print('Valor correto: ', teste_1)
