distance = float(input('Qual é a distância da sua viagem? '))

price = distance * 0.5 if distance <= 200 else distance * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(price))
