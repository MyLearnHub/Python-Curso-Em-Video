guys = list()
date = list()
small = big = 0

for count in range(0, 3):
    date.append(str(input('Nome: ')))
    date.append(int(input('Idade: ')))
    guys.append(date[:])
    date.clear()

for person in guys:
    if person[1] >= 21:
        print(f'{person[0]} é maior de idade.')
        big += 1
    else:
        print(f'{person[0]} é menor de idade.')
        small += 1

print(f'Temos {big} maiores e {small} menores de idade.')
