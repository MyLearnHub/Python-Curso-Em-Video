player = dict()
player['nome'] = str(input('Nome do jogador: '))
player['partidas'] = int(input(f'Quantas partidas {player["nome"]} jogou? '))
player['gols'] = []
totalGols = 0

for count in range(player['partidas']):
    gols = int(input(f'Quantos gols na partida {count}? '))
    totalGols += gols
    player['gols'].append(gols)
player['total'] = totalGols

print('-=' * 30)
print(player)
print('-=' * 30)
for key, value in player.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 30)
print(f'O jogador {player["nome"]} jogou {player["partidas"]} partidas.')
for count in range(player['partidas']):
    print(f'=> Na partida {count}, fez {player["gols"][count]} gols.')
print(f'Foi um total de {totalGols} gols.')
