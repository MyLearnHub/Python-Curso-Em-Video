velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade > 80.0:
    multa = (velocidade - 80) * 7
    print('Você foi multado! em R${:.2f}'.format(multa))
print('Tenha um bom dia!')
