from math import sqrt, ceil, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, ceil(raiz)))  # Arreedonda para cima
# print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz))) # Arredonda para baixo
