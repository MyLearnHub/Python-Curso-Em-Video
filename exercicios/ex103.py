def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
name = str(input('Nome do Jogador: '))
goals = input('Número de Gols: ')

if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

if name.strip() == '':
    ficha(gols=goals)
else:
    ficha(name, goals)
