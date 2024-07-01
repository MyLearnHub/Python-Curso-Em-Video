numbers = list()
positions_max = list()
positions_min = list()

for position in range(0, 5):
    number = int(input(f'Digite um valor para a posição {position}: '))
    numbers.append(number)

max_value = max(numbers)
min_value = min(numbers)

for key, value in enumerate(numbers):
    if value == max_value:
        positions_max.append(key)

    if value == min_value:
        positions_min.append(key)

print('=-' * 30)
print(f'Você digitou os valores {numbers}')
print(f'O maior valor digitado foi {max_value} nas posições ', end='')
for position in positions_max:
    print(f'{position}... ', end='')
print()
print(f'O menor valor digitado foi {min_value} nas posições ', end='')
for position in positions_min:
    print(f'{position}... ', end='')
print()
