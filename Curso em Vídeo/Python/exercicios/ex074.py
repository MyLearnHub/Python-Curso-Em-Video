from random import randint

numbers = ()
higher = 0
smallest = 0

while len(numbers) < 5:
    randomNumber = (randint(1, 10),)

    if len(numbers) < 1 or higher < randomNumber[0]:
        higher = randomNumber[0]

    if len(numbers) < 1 or smallest > randomNumber[0]:
        smallest = randomNumber[0]

    numbers += randomNumber

print(f'Os valores sorteados foram: ', end='')
for number in numbers:
    print(number, end=' ')
print(f'\nO maior valor sorteado foi {higher}')
# print(f'O maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {smallest}')
# print(f'O menor valor sorteado foi {min(numbers)}')
