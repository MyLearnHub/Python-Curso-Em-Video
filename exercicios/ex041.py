from datetime import date

birthYear = int(input('Ano de Nascimento: '))

age = date.today().year - birthYear

print('O atleta tem {} anos.'.format(age))
if age > 25:
    classification = 'MASTER'
elif age > 19:
    classification = 'SÊNIOR'
elif age > 14:
    classification = 'JUNIOR'
elif age > 9:
    classification = 'INFANTIL'
else:
    classification = 'MIRIM'
print('Classificação: {}'.format(classification))
