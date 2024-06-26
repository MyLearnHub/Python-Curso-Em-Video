from datetime import date

minor = 0
legalAge = 0

for person in range(1, 8):
    birthYear = int(input('Em que ano a {}ª pessoa nasceu?  '.format(person)))
    if date.today().year - birthYear < 18:
        minor += 1
    else:
        legalAge += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(legalAge))
print('E também tivemos {} pessoas menores de idade'.format(minor))
