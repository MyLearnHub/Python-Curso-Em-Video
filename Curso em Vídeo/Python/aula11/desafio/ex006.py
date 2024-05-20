number = int(input('\033[1;30;43mDigite um número: \033[m'))

print('\033[1;32mO dobro de {} vale {}.'.format(number, (number * 2)))
print('O triplo de {} vale {}.'.format(number, (number * 3)))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(number, (number ** (1/2))))
