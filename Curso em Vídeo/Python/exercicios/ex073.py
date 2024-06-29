teams = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {teams}')
print('-=' * 15)
print(f'Os 5 primeiros são {teams[:5]}')
print('-=' * 15)
print(f'Os últimos 4 são {teams[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(teams)}')
print('-=' * 15)
print(f'O Chapecoense está na {teams.index("Chapecoense") + 1}ª posição')
