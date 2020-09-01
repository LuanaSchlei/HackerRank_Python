#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
#
# Title: Map and Lambda Function
#
# Arquivo de Teste
#

# input_tamanho_lista = int(input())
input_tamanho_lista = '5'
input_tamanho_lista_int = int(input_tamanho_lista)
print(input_tamanho_lista_int)
    
fib_list = [0, 1]
fib = list(map(lambda x: fib_list.append(sum(fib_list[-2:])),
                range(2, input_tamanho_lista_int)))
print(fib_list)

list_cube = list(map(lambda x: pow(x, 3), fib_list))
print(list_cube)

print('--------------------------------')

cube = lambda x: pow(x, 3)
#cube = lambda x: print(x)

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]    
    fib_list = [0, 1]
    any(map(lambda x: fib_list.append(sum(fib_list[-2:])),
                range(2, n)))
    return fib_list                

if __name__ == '__main__':
    input_tamanho_lista = '1'
    n = int(input_tamanho_lista)
    # f_result = fibonacci(n)
    # print(f_result)
    print(list(map(cube, fibonacci(n))))
