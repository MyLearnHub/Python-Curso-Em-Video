valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = (valor / anos) / 12
porcentagemSalario = (salario * 30) / 100

if prestacao > porcentagemSalario:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
