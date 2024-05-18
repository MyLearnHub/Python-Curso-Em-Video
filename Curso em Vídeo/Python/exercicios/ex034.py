salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    # novo = salario * 1.15
    novo = salario + (salario * 15 / 100)
else:
    # novo = salario * 1.10
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
