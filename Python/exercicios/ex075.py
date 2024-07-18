numbers = ()
even = ()

while len(numbers) < 4:
    number = int(input('Digite um número: '))
    numbers += (number,)

    if number % 2 == 0:
        even += (number,)

print(f'O valor 9 apareceu {numbers.count(9)} vezes')

if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {even}')

'''
numbers = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))

print(f'Você digitou o valor {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes')
print(f'O valor 3 apareceu na {numbers.index(3) + 1}ª posição')

if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')
for number in numbers:
    if number % 2 == 0:
        print(number, end='')
'''