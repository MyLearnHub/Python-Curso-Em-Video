wage = float(input('Qual é o salário do funcionário? R$'))

newWage = wage * 1.15 if wage <= 1250 else wage * 1.10
    
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(wage, newWage))
