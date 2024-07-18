players = list()

while True:
    player = dict()

    print('-' * 30)
    player['nome'] = str(input('Nome do jogador: '))
    player['partidas'] = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    player['gols'] = []
    totalGols = 0

    for count in range(player['partidas']):
        gols = int(input(f'Quantos gols na partida {count}? '))
        totalGols += gols
        player['gols'].append(gols)
    player['total'] = totalGols

    players.append(player.copy())
    player.clear()

    continuation = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuation in 'Nn':
        break

print('-=' * 30)
print(f'{'cod':<4}{'nome':<10}{'gols':<10}{'total':>6}')
print('-' * 26)
for key, player in enumerate(players):
    print(f'{key:<4}{player["nome"]:<10}{player["gols"]}{' ':<3}{player["total"]:>6}')

while True:
    print('-' * 30)
    playerIndex = int(input('Mostrar dados de qual jogador? '))

    if playerIndex == 999:
        break
    elif playerIndex >= len(players):
        print('ERRO! Não existe jogador com código 5! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {players[playerIndex]["nome"]}:')
        for key, value in enumerate(players[playerIndex]['gols']):
            print(f'    No jogo {key} fez {value} gols.')
print('<<< VOLTE SEMPRE >>>')
