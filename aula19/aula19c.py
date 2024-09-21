state = dict()
brasil = list()

for count in range(0, 3):
    state['uf'] = str(input('Unidade Federativa: '))
    state['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(state.copy())
print(brasil)

for estate in brasil:
    for key, value in estate.items():
        print(f'O campo {key} tem valor {value}.')
    for values in estate.values():
        print(values, end=' ')
    print()
