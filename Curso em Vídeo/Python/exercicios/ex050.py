numberSum = 0
for count in range(0, 6):
    number = int(input('Digite um número: '))

    if number % 2 == 0:
        numberSum += number

print('Soma dos número pares: {}'.format(numberSum))
