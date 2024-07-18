numbers = list()

while True:
    numbers.append(int(input(f'Digite um valor: ')))

    continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuation in 'Nn':
        break

print('-=' * 30)
numbers.sort(reverse=True)
print(f'Você digitou {len(numbers)} elementos')
print(f'Os valores em ordem decrescente são {numbers}')
if 5 in numbers:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
