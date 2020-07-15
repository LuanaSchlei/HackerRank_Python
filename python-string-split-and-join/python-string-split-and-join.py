

def split_and_join(line):
    saida = ''
    line_split = line.split(' ')
    saida = '-'.join(line_split)
    return saida

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result) 

# TODO: alguma coisa
