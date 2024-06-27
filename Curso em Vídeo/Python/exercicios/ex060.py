number = int(input('Digite um número: '))
multiplier = number

while multiplier > 1:
    multiplier -= 1
    number *= multiplier
print('Fatorial: {}'.format(number))

# Solução com for
'''
number = int(input('Digite um número: '))
fatorial = 1

for i in range(1, number + 1):
    fatorial *= i

print('Fatorial: {}'.format(fatorial))
'''
