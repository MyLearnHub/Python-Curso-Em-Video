currentPrice = float(input('Qual é o preço do produto? '))

newPrice = currentPrice * 0.95

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(currentPrice, newPrice))

# 10 * 5 / 100  # 0.5
# 1500 * 10 / 100  # 150.0
# 875 * 15 / 100  # 131.25
