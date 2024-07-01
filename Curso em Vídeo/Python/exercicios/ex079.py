numbers = list()
continuation = 'S'

while continuation == 'S':
    number = int(input(f'Digite um valor: '))

    if number in numbers:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numbers.append(number)
        print('Valor adicionado com sucesso...')

    continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print('-=' * 30)
numbers.sort()
print(f'Você digitou os valores {numbers}')
