from datetime import datetime

anoNascimento = int(input('Digite o ano de nascimento: '))
idade = datetime.now().year - anoNascimento

if idade > 20:
    print('Master')
elif idade > 19:
    print('Sênior')
elif idade > 14:
    print('Junior')
elif idade > 9:
    print('Infantil')
else:
    print('Mirim')
