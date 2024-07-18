from random import randint

print('\033[1;34m-=-' * 20)
print('\033[1;31mVou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('\033[1;34m-=-' * 20)

computerNumber = randint(0, 5)
playerNumber = int(input('\033[1;32mEm que número eu pensei? '))

if playerNumber == computerNumber:
    print('PARÁBENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computerNumber, playerNumber))
