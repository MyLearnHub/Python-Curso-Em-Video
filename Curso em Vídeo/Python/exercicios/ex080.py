numbers = list()

for count in range(5):
    number = int(input(f'Digite um valor: '))

    inserted = False
    for position in range(len(numbers)):
        if number < numbers[position]:
            numbers.insert(position, number)
            print(f'Adicionado na posição {position} da lista...')
            inserted = True
            break

    if not inserted:
        numbers.append(number)
        print('Adicionado ao final da lista...')

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {numbers}')
