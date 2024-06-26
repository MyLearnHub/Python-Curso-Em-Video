countAge = 0
countFemale = 0
olderAge = 0
olderName = ""

for c in range(0, 4):
    name = str(input('Digite o nome: '))
    age = int(input('Digite a idade: '))
    gender = str(input('Digite o sexo: '))

    countAge += age
    if gender == 'M' and olderAge < age:
        olderName = name
    if gender == 'F' and age < 20:
        countFemale += 1

average = countAge // 4

print('Média de idade: {}'.format(average))
print('Homem mais velho: {}'.format(olderName))
print('Mulheres com menos de 20 anos: {}'.format(countFemale))
