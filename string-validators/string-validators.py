#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/string-validators/problem
#
# Title: String Validators
#


if __name__ == '__main__':
    s = input()
    
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
    
