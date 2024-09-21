people = list()
ageSum = 0

while True:
    person = dict()
    person['nome'] = str(input('Nome: '))
    while True:
        person['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if person['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    person['idade'] = int(input('Idade: '))

    ageSum += person['idade']

    people.append(person.copy())
    person.clear()

    while True:
        continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuation in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuation in 'Nn':
        break

ageAverage = ageSum / len(people)

print('-=' * 30)
print(f'A) Ao todo temos {len(people)} pessoas cadastradas.')
print(f'B) A média de idade é de {ageAverage} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for person in people:
    if person['sexo'] == 'F':
        print(f'{person['nome']}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for person in people:
    if person['idade'] > ageAverage:
        for key, values in person.items():
            print(f' {key} = {values};', end=' ')
        print()
print('<< ENCERRADO >>')
