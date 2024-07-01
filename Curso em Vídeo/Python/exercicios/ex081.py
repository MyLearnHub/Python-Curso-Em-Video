numbers = list()
continuation = 'S'

while continuation == 'S':
    number = int(input(f'Digite um valor: '))
    numbers.append(number)

    continuation = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print('-=' * 30)
numbers.sort(reverse=True)
print(f'Você digitou {len(numbers)} elementos')
print(f'Os valores em ordem decrescente são {numbers}')
if 5 in numbers:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
    print('Não achei o número 5')
