from random import randint
from time import sleep

print('-' * 30)
print(f'{'JOGO NA MEGA SENA':^30}')
print('-' * 30)

amountGames = int(input('Quantos jogos você quer que eu sorteie? '))
games = list()
count = 0

while count < amountGames:
    game = list()
    for number in range(0, 6):
        game.append(randint(1, 60))

    games.append(game[:])
    game.clear()

    count += 1

print(f'{'  SORTEANDO 4 JOGOS  ':-^30}')
for key, game in enumerate(games):
    game.sort()
    print(f'Jogo {key + 1}: {game}')
    sleep(1)
