from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
computerNumber = randint(0, 10)
correct = False
attempts = 0

while not correct:
    playerNumber = int(input('Qual é seu palpite? '))

    attempts += 1

    if playerNumber == computerNumber:
        correct = True
    elif playerNumber < computerNumber:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns'.format(attempts))
