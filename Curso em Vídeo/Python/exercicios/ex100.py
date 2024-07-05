from random import randint

numbers = list()


def sorteia():
    for count in range(0, 5):
        number = randint(1, 10)
        numbers.append(number)

    somaPar(*numbers)


def somaPar(*values):
    soma = 0

    for value in values:
        if value % 2 == 0:
            soma += value

    print(soma)

sorteia()
