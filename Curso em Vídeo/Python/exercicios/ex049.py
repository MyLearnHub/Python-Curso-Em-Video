number = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)
for position in range(1, 11):
    print('{} x {:2} = {}'.format(number, position, number * position))
print('-' * 12)
