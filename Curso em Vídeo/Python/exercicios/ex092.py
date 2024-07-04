from datetime import date

worker = dict()
worker['nome'] = str(input('Nome: '))
birthYear = int(input('Ano de Nascimento: '))
worker['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
worker['idade'] = date.today().year - birthYear

if worker['ctps'] != 0:
    worker['contratação'] = int(input('Ano de Contratação: '))
    worker['salário'] = float(input('Salário: R$ '))
    worker['aposentadoria'] = worker['contratação'] - birthYear + 35

print('-=' * 30)
print(worker)
for key, value in worker.items():
    print(f'{key} tem o valor {value}')
