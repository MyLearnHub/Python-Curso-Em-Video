from random import randint
from time import sleep


def sorteia(numbersList):
    print('Sorteando 5 valores da lista', end='')
    for count in range(0, 5):
        number = randint(1, 10)
        numbersList.append(number)
        print(f'{number} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(valuesList):
    soma = 0
    for value in valuesList:
        if value % 2 == 0:
            soma += value
    print(f'Somando os valores pares de {valuesList}, temos {soma}')

numbers = list()
sorteia(numbers)
somaPar(numbers)
