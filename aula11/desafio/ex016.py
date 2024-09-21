from math import trunc

number = float(input('\033[1;40mDigite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}\033[m'.format(number, trunc(number)))
