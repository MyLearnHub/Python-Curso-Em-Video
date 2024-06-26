from datetime import date

minor = 0
legalAge = 0

for count in range(0, 7):
    birthYear = int(input('Ano de nascimento: '))
    if date.today().year - birthYear < 18:
        minor += 1
    else:
        legalAge += 1

print('Menores de idade: {}'.format(minor))
print('Maiores de idade: {}'.format(legalAge))
