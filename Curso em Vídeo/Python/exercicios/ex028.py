from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)

computerNumber = randint(0, 5)  # Faz o computador "PENSAR"
playerNumber = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(3)
if playerNumber == computerNumber:
    print('PARÁBENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computerNumber, playerNumber))
