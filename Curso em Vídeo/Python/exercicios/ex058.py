from random import randint
from time import sleep

computerNumber = 0
playerNumber = 1
attempts = 0

while playerNumber != computerNumber:
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
    print('-=-' * 20)
    computerNumber = randint(0, 5)
    playerNumber = int(input('Em que número eu pensei? '))

    attempts += 1

    print('PROCESSANDO...')
    sleep(3)
    if playerNumber == computerNumber:
        print('PARÁBENS! Você conseguiu me vencer!')
    else:
        print('GANHEI! Eu pensei no número {} e não no {}!'.format(computerNumber, playerNumber))
print('Foram necessárias {} tentativas para acertar'.format(attempts))
