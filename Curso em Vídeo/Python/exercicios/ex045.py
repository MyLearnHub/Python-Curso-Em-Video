from random import choice
from time import sleep

print('''Suas opções:
PEDRA
PAPEL
TESOURA''')
player = str(input('Qual é a sua jogada? ')).upper()

options = ['PEDRA', 'PAPEL', 'TESOURA']
computer = choice(options)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print('-=' * 11)
print('Computador jogou {}'.format(computer))
print('Jogador jogou {}'.format(player))
print('-=' * 11)
if player == computer:
    print("EMPATE")
elif player == 'TESOURA' and computer == 'PAPEL' or player == 'PAPEL' and computer == 'PEDRA' or player == 'PEDRA' and computer == 'TESOURA':
    print('JOGADOR VENCE')
else:
    print('COMPUTADOR VENCE')


# Usando números ao invés de String
'''
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)
print('Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA')
player = int(input('Qual é a sua jogada? '))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print('-=' * 11)
print('O computador jogou {}'.format(itens[computer]))
print('O jogador jogou {}'.format(itens[player]))
print('-=' * 11)

if computer == 0: # computador jogou PEDRA
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computer == 1: # computador jogou PAPEL
    if player == 0:
        print('COMPUTADOR VENCE')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
else: # computador jogou TESOURA
    if player == 0:
        print('JOGADOR VENCE')
    elif player == 1:
        print('COMPUTADOR VENCE')
    elif player == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
'''
