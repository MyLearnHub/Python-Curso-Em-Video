a = [2, 3, 4, 7]
# b = a  # Cria uma ligação entre as 2 listas
b = a[:]  # Cria uma cópia entre as 2 listas
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
