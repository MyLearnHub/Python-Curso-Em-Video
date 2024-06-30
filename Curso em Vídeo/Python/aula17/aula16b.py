# values = list(range(1, 11))  # Cria uma lista de valores de 1 a 10
# values = []  # Cria uma lista vazia
values = list()
for cont in range(0, 5):
    values.append(int(input('Digite um valor: ')))

for key, value in enumerate(values):
    print(f'Na posição {key} encontrei o valor {value}!')
print('Cheguei ao final da lista.')
