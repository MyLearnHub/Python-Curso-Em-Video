number = int(input('Digite um número para ver sua tabuada: '))

for multiplier in range(1, 11):
    print('{} x {:2} = {}'.format(number, multiplier, number * multiplier))
