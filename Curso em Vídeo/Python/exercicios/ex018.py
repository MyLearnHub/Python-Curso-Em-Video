from math import cos, sin, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, seno))
coseno = cos(radians(angulo))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, coseno))
tangente = tan(radians(angulo))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
