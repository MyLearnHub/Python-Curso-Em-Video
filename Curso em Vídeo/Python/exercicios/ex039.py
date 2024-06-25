from datetime import date

birthYear = int(input('Ano de nascimento: '))

currentYear = date.today().year
age = currentYear - birthYear

print('Quem nasceu em {} tem {} anos em {}.'.format(birthYear, age, currentYear))
if age == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif age < 18:
    years = 18 - age
    missingYears = currentYear + years
    print('Ainda faltam {} anos para o alistamento'.format(years))
    print('Seu alistamento será em {}.'.format(missingYears))
else:
    years = age - 18
    missingYears = currentYear - years
    print('Você já deveria ter se alistado há {} anos'.format(years))
    print('Seu alistamento foi em {}.'.format(missingYears))
