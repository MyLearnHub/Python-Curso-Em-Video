from math import cos, sin, tan, radians

angle = float(input('Digite o ângulo que você deseja: '))

sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angle, sine))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angle, cosine))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angle, tangent))
