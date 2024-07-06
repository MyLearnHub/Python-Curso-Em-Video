def ficha(nome='<desconhecido>', gols=0):
    if not nome:
        nome = '<desconhecido>'

    if gols.isdigit():
        gols = int(gols)
    else:
        gols = 0

    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('-' * 30)
name = str(input('Nome do Jogador: '))
goals = input('Número de Gols: ')
print(ficha(name, goals))
