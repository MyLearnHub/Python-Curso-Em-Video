snack = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# snack = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim' # O Python aceita a declaração sem parentenses

# Tuplas são imutáveis
# snack[1] = 'Refrigerante'  # ERRO
print(snack)
print(snack[1])
print(snack[-2])
print(snack[1:3])
print(snack[2:])
print(snack[:2])
print(snack[-2:])
print(snack[-3:])
print(len(snack))

for food in snack:
    print(f'Eu vou comer {food}')

for count in range(0, len(snack)):
    print(f'Eu vou comer {snack[count]} na posição {count}')

for position, food in enumerate(snack):
    print(f'Eu vou comer {food} na posição {position}')

print('Comi pra caramba!')

print(sorted(snack))
