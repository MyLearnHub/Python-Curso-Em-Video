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
        while True:
            valueSorted = randint(1, 60)
            if valueSorted not in game:
                game.append(valueSorted)
                break

    games.append(game[:])
    game.clear()

    count += 1

print('-=' * 3,  f'SORTEANDO {amountGames} JOGOS', '-=' * 3)
for key, game in enumerate(games):
    game.sort()
    print(f'Jogo {key + 1}: {game}')
    sleep(1)
