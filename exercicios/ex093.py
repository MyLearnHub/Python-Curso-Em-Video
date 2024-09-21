player = dict()
player['nome'] = str(input('Nome do jogador: '))
matches = int(input(f'Quantas partidas {player["nome"]} jogou? '))
player['gols'] = []

for count in range(matches):
    player['gols'].append(int(input(f'   Quantos gols na partida {count}? ')))
player['total'] = sum(player['gols'])

print('-=' * 30)
print(player)
print('-=' * 30)
for key, value in player.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 30)
print(f'O jogador {player["nome"]} jogou {matches} partidas.')
for count in range(matches):
    print(f'    => Na partida {count}, fez {player["gols"][count]} gols.')
print(f'Foi um total de {sum(player['gols'])} gols.')
