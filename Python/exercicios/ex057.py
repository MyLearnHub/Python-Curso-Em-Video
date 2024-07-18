gender = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]

while gender not in 'MmFf':
    gender = str(input('Dados inválidos. Por favor, insira seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(gender))
