
import curses.ascii


if __name__ == '__main__':
    s = 'qA2'
    

    def checar_tipo(teste_tipo_fun):
        for caracter_atual in s:
            if teste_tipo_fun(caracter_atual):
                return True
        return False

    print(checar_tipo(curses.ascii.isalnum))
    print(checar_tipo(curses.ascii.isalpha))

    achouAlfanum = False
    for caracter_atual in s:
        if caracter_atual.isalnum():
            achouAlfanum = True
    print(achouAlfanum)

    achouAlfabet = False
    for caracter_atual in s:
        if caracter_atual.isalpha():
            achouAlfabet = True
    print(achouAlfabet)
        
    achouDigito = False
    for caracter_atual in s:
        if caracter_atual.isdigit():
            achouDigito = True
    print(achouDigito)
    
    achouMinusculo = False
    for caracter_atual in s:
        if caracter_atual.islower():
            achouMinusculo = True
    print(achouMinusculo)
    
    achouMaiuscula = False
    for caracter_atual in s:
        if caracter_atual.isupper():
            achouMaiuscula = True
    print(achouMaiuscula)
    
