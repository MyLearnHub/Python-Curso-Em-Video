numbers = ()
even = ()

while len(numbers) < 4:
    number = int(input('Digite um número: '))
    numbers += (number,)

    if number % 2 == 0:
        even += (number,)

if numbers.count(9):
    print(f'O valor 9 apareceu {numbers.count(9)} vezes')
else:
    print('O valor 9 apareceu 0 vezes')

if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {even}')
