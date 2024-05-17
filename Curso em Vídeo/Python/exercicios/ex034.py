salario = float(input('Digite seu salário: '))
if salario > 1250:
    salario = salario * 1.10
else:
    salario = salario * 1.15
print('Seu novo salário é: R${}'.format(salario))
