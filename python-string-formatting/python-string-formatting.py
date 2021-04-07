#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/python-string-formatting/problem
#
# Title: String Formatting
#

def print_formatted(number):
    tamanho_n_bin = len(bin(number)) - 2
    for cada_linha in range(1, number + 1):
        number_decimal = cada_linha 
        number_octal = oct(cada_linha)[2:] 
        number_hexadecimal = hex(cada_linha)[2:] 
        number_binary = bin(cada_linha)[2:] 
        espaco_dec = str(number_decimal).rjust(tamanho_n_bin, ' ')
        espaco_oct = str(number_octal).rjust(tamanho_n_bin, ' ')
        espaco_hex = str(number_hexadecimal).upper().rjust(tamanho_n_bin, ' ')
        espaco_bin = str(number_binary).rjust(tamanho_n_bin, ' ')
            
        print(espaco_dec, espaco_oct, espaco_hex, espaco_bin)

    return

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

