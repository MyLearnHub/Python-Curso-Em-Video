matriz = [[], [], []]
evenSum = columnSum = 0

for row in range(0, 3):
    for column in range(0, 3):
        matriz[row].append(int(input(f'Digite um valor para [{row}, {column}]: ')))

        if matriz[row][column] % 2 == 0:
            evenSum += matriz[row][column]

        if column == 2:
            columnSum += matriz[row][2]

print('-=' * 30)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matriz[row][column]:^5}]', end='')
    print()
print('-=' * 30)

print(f'A soma dos valores pares é {evenSum}')
print(f'A soma dos valores da terceira coluna é {columnSum}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
