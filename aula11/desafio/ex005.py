number = int(input('\033[1;32;40mDigite um número: '))

print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}\033[m'.format(number, (number - 1), (number + 1)))
