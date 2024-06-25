from math import hypot

opposite = float(input('Comprimento do cateto oposto: '))
adjacent = float(input('Comprimento do cateto adjacente: '))

hypotenuse = hypot(opposite, adjacent)

print('A hipotenusa vai medir {:.2f}'.format(hypotenuse))

"""
opposite = float(input('Comprimento do cateto oposto: '))
adjacent = float(input('Comprimento do cateto adjacente: '))

hypotenuse = (opposite ** 2 + adjacent ** 2) ** (1 / 2)

print('A hipotenusa vai medir {:.2f}'.format(hypotenuse))
"""  # Sem Biblioteca
