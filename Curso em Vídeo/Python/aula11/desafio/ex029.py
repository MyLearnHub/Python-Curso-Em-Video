speed = float(input('\033[1;34;40mQual é a velocidade atual do carro? '))

if speed > 80:
    penalty = (speed - 80) * 7

    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(penalty))

print('Tenha um bom dia! Dirija com segurança')
