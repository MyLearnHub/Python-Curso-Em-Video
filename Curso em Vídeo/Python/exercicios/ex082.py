numbers = list()
evens = list()
odds = list()
continuation = 'S'

while continuation == 'S':
    number = int(input(f'Digite um valor: '))
    numbers.append(number)

    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

    continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print(f'A lista completa é {numbers}')
print(f'A lista de pares é {evens}')
print(f'A lista de ímpares é {odds}')
