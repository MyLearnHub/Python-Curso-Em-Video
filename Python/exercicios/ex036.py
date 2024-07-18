house = float(input('Valor da casa: R$'))
wage = float(input('Salário do comprador: R$'))
years = int(input('Quantos anos de financiamento? '))

payment = house / (years * 12)
minimum = wage * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(house, years, payment))
if payment <= minimum:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
