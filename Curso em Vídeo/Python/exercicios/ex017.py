from math import hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))
