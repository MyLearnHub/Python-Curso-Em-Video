people = list()
ageSum = 0

while True:
    person = dict()
    person['nome'] = str(input('Nome: '))
    person['sexo'] = str(input('Sexo: [M/F] ')).upper()
    person['idade'] = int(input('Idade: '))

    ageSum += person['idade']

    people.append(person.copy())
    person.clear()

    continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuation in 'Nn':
        break

ageAverage = ageSum / len(people)

print('-=' * 30)
print(f'- O grupo tem {len(people)} pessoas.')
print(f'- A média de idade é de {ageAverage} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for person in people:
    if person['sexo'] == 'F':
        print(f'{person['nome']}', end=' ')
print()
print(f'- Lista das pessoas que estão acima da média:')
for person in people:
    if person['idade'] > ageAverage:
        for key, values in person.items():
            print(f'{key} = {values};', end=' ')
        print()
print('<< ENCERRADO >>')
