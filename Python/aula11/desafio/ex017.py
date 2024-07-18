from math import hypot

opposite = float(input('\033[1;34mComprimento do cateto oposto: '))
adjacent = float(input('Comprimento do cateto adjacente: '))

hypotenuse = hypot(opposite, adjacent)

print('A hipotenusa vai medir {:.2f}'.format(hypotenuse))
