numbers = list()
biggest = 0
smallest = 0

for position in range(0, 5):
    numbers.append(int(input(f'Digite um valor para a posição {position}: ')))

    if position == 0:
        biggest = smallest = numbers[position]
    else:
        if numbers[position] > biggest:
            biggest = numbers[position]
        if numbers[position] < smallest:
            smallest = numbers[position]
print('=-' * 30)
print(f'Você digitou os valores {numbers}')
print(f'O maior valor digitado foi {biggest} nas posições ', end='')
for key, value in enumerate(numbers):
    if value == biggest:
        print(f'{key}... ', end='')
print()
print(f'O menor valor digitado foi {smallest} nas posições ', end='')
for key, value in enumerate(numbers):
    if value == smallest:
        print(f'{key}... ', end='')
print()
