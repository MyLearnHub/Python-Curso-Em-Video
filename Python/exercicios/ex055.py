heaviest = 0.0
lighter = 0.0

for person in range(1, 6):
    weigth = float(input('Peso da {}ª pessoa: '.format(person)))
    if person == 1:
        heaviest = weigth
        lighter = weigth
    else:
        if weigth > heaviest:
            heaviest = weigth

        if weigth < lighter:
            lighter = weigth

print('O maior peso lido foi de {:.1f}Kg'.format(heaviest))
print('O menor peso lido foi de {:.1f}Kg'.format(lighter))
