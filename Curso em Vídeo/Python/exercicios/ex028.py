from random import randint

num = int(input('Estou pensando em um número de 0 a 5. Adivinhe qual é: '))
numEscolhido = randint(0, 5)
if numEscolhido == num:
    print('Parábens você acertou o número!')
else:
    print('Que pena, você errou...')
