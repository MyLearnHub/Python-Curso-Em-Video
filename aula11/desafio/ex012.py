currentPrice = float(input('\033[1mQual é o preço do produto? '))

newPrice = currentPrice * 0.95

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(currentPrice, newPrice))
