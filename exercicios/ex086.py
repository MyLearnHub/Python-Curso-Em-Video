matriz = [[], [], []]

for row in range(0, 3):
    for column in range(0, 3):
        matriz[row].append(int(input(f'Digite um valor para [{row}, {column}]: ')))

print('-=' * 30)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matriz[row][column]:^5}]', end='')
    print()
