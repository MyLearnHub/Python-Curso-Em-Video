maior = 0.0
menor = 100000

for c in range(0, 5):
    weigth = float(input('Digite o peso: '))
    if weigth > maior:
        maior = weigth

    if weigth < menor:
        menor = weigth

print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))
