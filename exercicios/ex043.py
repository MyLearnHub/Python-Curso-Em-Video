weight = float(input('Qual é seu peso? (Kg) '))
height = float(input('Qual é sua altura? (m) '))

imc = weight / (height ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
else:
    if imc < 18.5:
        situation = 'ABAIXO DO PESO normal'
    elif 25 <= imc < 30:
        situation = 'em SOBREPESO'
    elif 30 <= imc < 40:
        situation = 'em OBESIDADE!'
    else:
        situation = 'em OBESIDADE MÓRBIDA, cuidado!'

    print('Você está {}'.format(situation))
