numbers = list()
evens = list()
odds = list()

while True:
    numbers.append(int(input(f'Digite um valor: ')))

    continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuation in 'Nn':
        break

for key, value in enumerate(numbers):
    if value % 2 == 0:
        evens.append(value)
    else:
        odds.append(value)

print('-=' * 30)
print(f'A lista completa é {numbers}')
print(f'A lista de pares é {evens}')
print(f'A lista de ímpares é {odds}')

# Minha solução

'''
numbers = list()
evens = list()
odds = list()

while True:
    number = int(input(f'Digite um valor: '))
    numbers.append(number)

    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

    continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuation in 'Nn':
        break
    
print('-=' * 30)
print(f'A lista completa é {numbers}')
print(f'A lista de pares é {evens}')
print(f'A lista de ímpares é {odds}')
'''