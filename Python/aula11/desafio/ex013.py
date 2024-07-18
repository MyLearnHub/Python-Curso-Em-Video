wage = float(input('\033[4mQual é o salário do funcionário? R$'))

newWage = wage * 1.15

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(wage, newWage))
