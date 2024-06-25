valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = (valor / anos) / 12
porcentagemSalario = (salario * 30) / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestacao))

if prestacao > porcentagemSalario:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
