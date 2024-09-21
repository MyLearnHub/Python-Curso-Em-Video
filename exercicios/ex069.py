eighteenAge = mans = womans = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    age = int(input('Idade: '))
    gender = ' '
    while gender not in 'MmFf':
        gender = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if age > 18:
        eighteenAge += 1

    if gender == 'M':
        mans += 1

    if gender == 'F' and age < 20:
        womans += 1

    print('-' * 30)
    option = ' '
    while option not in 'SN':
        option = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if option == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {eighteenAge}')
print(f'Ao todo temos {mans} homens cadastrados')
print(f'E temos {womans} mulheres com menos de 20 anos')
