people = list()
heavy = light = 0

while True:
    person = list()
    person.append(str(input('Nome: ')))
    person.append(float(input('Peso: ')))

    if len(people) == 0:
        heavy = light = person[1]
    else:
        if person[1] > heavy:
            heavy = person[1]

        if person[1] < light:
            light = person[1]

    people.append(person[:])
    person.clear()

    continuation = str(input('Quer continuar? [S/N] '))
    if continuation in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(people)} pessoas.')
print(f'O maior peso foi de {heavy}Kg. Peso de ', end='')
for weight in people:
    if weight[1] == heavy:
        print(f'[{weight[0]}]', end=' ')
print()
print(f'O menor peso foi de {light}Kg. Peso de ', end='')
for weight in people:
    if weight[1] == light:
        print(f'[{weight[0]}]', end=' ')
