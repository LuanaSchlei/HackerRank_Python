

def swap_case(s):
    saida = ''
    for i in s:
        if i.islower():
            saida += i.upper()
        elif i.isupper():
            saida += i.lower()
        else:
            saida += i
    return saida

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)