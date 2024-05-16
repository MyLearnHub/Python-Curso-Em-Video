from math import cos, sin, tan, radians

a = float(input('Digite um ângulo: '))
seno = sin(radians(a))
coseno = cos(radians(a))
tangente = tan(radians(a))
print('O seno de {} é: {}'.format(a, seno))
print('O coseno de {} é: {}'.format(a, coseno))
print('A tangente de {} é: {}'.format(a, tangente))
