countAge = 0
olderAge = 0
olderName = ""
countFemale = 0

for person in range(1, 5):
    print('----- {}ª PESSOA -----'.format(person))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip().upper()

    countAge += age
    if gender == 'M' and olderAge < age:
        olderAge = age
        olderName = name
    if gender == 'F' and age < 20:
        countFemale += 1

average = countAge / 4

print('A média de idade do grupo é de {:.1f} anos'.format(average))
print('O homem mais velho tem {} anos e se chama {}.'.format(olderAge, olderName))
print('Ao todo são {} mulheres com menos de 20 anos'.format(countFemale))
