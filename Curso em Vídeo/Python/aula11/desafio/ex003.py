number1 = int(input('\033[1;30;43mDigite um valor: '))
number2 = int(input('Digite outro valor: \033[m'))

total = number1 + number2

print('\033[1;30;45mA soma entre {} e {} vale {}\033[m'.format(number1, number2, total))
