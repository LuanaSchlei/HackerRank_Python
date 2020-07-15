

def print_formatted(number):
    for cada_linha in range(1, number + 1):
        number_decimal = cada_linha
        number_octal = oct(cada_linha)[2:]
        number_hexadecimal = hex(cada_linha)[2:]
        number_binary = bin(cada_linha)[2:]

        print(number_decimal, number_octal, number_hexadecimal, number_binary)
  
    return


if __name__ == '__main__':
    n = 17
    print_formatted(n)