wage = float(input('Qual é o salário do funcionário? R$'))

if wage <= 1250:
    # newWage = wage * 1.15
    newWage = wage + (wage * 15 / 100)
else:
    # novo = wage * 1.10
    newWage = wage + (wage * 10 / 100)
# newWage = wage * 1.15 if wage <= 1250 else wage * 1.10

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(wage, newWage))
