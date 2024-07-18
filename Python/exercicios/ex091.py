from operator import itemgetter
from random import randint
from time import sleep

moves = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}

print('Valores sorteados:')
for key, value in moves.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)

ranking = sorted(moves.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for key, value in enumerate(ranking):
    print(f'   {key + 1}º lugar: {value[0]} com {value[1]}')
    sleep(1)
