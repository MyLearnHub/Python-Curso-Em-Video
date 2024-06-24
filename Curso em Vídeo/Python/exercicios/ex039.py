from datetime import datetime

anoNascimento = int(input('Digite o ano de nascimento: '))
idade = datetime.now().year - anoNascimento

if idade < 18:
    print('Vai se alistar ao serviço militar em {} anos'.format(18 - idade))
elif idade == 18:
    print('Ta na hora de se alistar')
else:
    print('Passou do tempo de se alistar a {} anos'.format(idade - 18))
