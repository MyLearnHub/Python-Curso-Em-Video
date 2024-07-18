from math import factorial

number = int(input('Digite um número para calcular sua Fatorial: '))

result = factorial(number)

print('O fatorial de {} é {}'.format(number, result))

# Solução com while
'''
number = int(input('Digite um número para calcular seu Fatorial: '))
multiplier = number
result = 1
print('Calculando {}! = '.format(number), end='')

while multiplier > 0:
    print('{}'.format(multiplier), end='')
    print(' x ' if multiplier > 1 else ' = ', end='')
    result *= multiplier
    multiplier -= 1
print('{}'.format(result))
'''

# Solução com for
'''
number = int(input('Digite um número: '))
fatorial = 1

for i in range(1, number + 1):
    fatorial *= i

print('Fatorial: {}'.format(fatorial))
'''
