from operator import itemgetter
from random import randint
from time import sleep

moves = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

print('Valores sorteados:')
for key, value in moves.items():
    print(f'O {key} tirou {value}')
    sleep(1)

sorted_moves = dict(sorted(moves.items(), key=itemgetter(1), reverse=True))

print('Ranking dos jogadores:')
for count, (key, value) in enumerate(sorted_moves.items()):
    print(f'{count + 1}º lugar {key} com {value}')
    sleep(1)
