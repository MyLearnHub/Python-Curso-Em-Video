people = list()
heavy = list()
light = list()

while True:
    person = list()
    person.append(str(input('Nome: ')))
    person.append(float(input('Peso: ')))

    if len(people) == 0:
        heavy.append(person[:])
        light.append(person[:])
    else:
        if person[1] == heavy[0][1]:
            heavy.append(person[:])
        elif person[1] > heavy[0][1]:
            heavy.clear()
            heavy.append(person[:])

        if person[1] == light[0][1]:
            light.append(person[:])
        elif person[1] < light[0][1]:
            light.clear()
            light.append(person[:])

    people.append(person[:])
    person.clear()

    continuation = str(input('Quer continuar? [S/N] '))
    if continuation in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(people)} pessoas.')
print(f'O maior peso foi de {heavy[0][1]}Kg. Peso de ', end='')
for person in heavy:
    print(f'{person[0]}', end=' ')
print()
print(f'O menor peso foi de {light[0][1]}Kg. Peso de ', end='')
for person in light:
    print(f'{person[0]}', end=' ')
