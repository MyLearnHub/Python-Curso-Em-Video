"""
cont = 1
while cont <= 5:
    print(cont, ' -> ', end='')
    cont += 1
print('Acabou')
"""

number = numberSum = 0
while True:
    number = int(input('Digite um número: '))

    if number == 999:
        break

    numberSum += number

# print('A soma vale {}'.format(numberSum))
print(f'A soma vale {numberSum}')
