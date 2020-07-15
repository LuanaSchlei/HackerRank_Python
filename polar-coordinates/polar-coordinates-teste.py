
import cmath

valor_entrada = '1-1j'
#valor_entrada = input()
valor_entrada_strip = valor_entrada.strip()
valor_entrada_split = valor_entrada_strip.split('+')
x, y = 0, 0
if len(valor_entrada_split) == 1:
    valor_entrada_split = valor_entrada_strip.split('-')
    if len(valor_entrada_split) == 3:
        x = int(valor_entrada_split[1]) * -1
        aux_y = valor_entrada_split[2][:-1]
        y = int(aux_y) * -1
    elif len(valor_entrada_split) == 2:
        x = int(valor_entrada_split[0]) 
        aux_y = valor_entrada_split[1][:-1]
        y = int(aux_y) * -1
else:
    x = int(valor_entrada_split[0])
    aux_y = valor_entrada_split[1][:-1]
    y = int(aux_y)



# Primeiro numeros reais
#x = 1
#y = 2

# convertendo em complex number
komplex_number = complex(x, y)

# convertendo em polar number
polar_coordinates = cmath.polar(komplex_number)
polar_coordinates_string = map(lambda x: str(x), polar_coordinates)
resultado = '\n'.join(polar_coordinates_string)
print(resultado)