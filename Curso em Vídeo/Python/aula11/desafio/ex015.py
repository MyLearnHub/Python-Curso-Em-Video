days = int(input('\033[7;30mQuantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

valueToPay = (days * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}\033[m'.format(valueToPay))
