gender = ''

while gender != 'M' and gender != 'F':
    gender = str(input('Digite o seu sexo: ')).upper()

    if gender != 'M' and gender != 'F':
        print('Sexo inválido, tente novamente')

print('Muito bem, seu genêro é {}'.format(gender))
