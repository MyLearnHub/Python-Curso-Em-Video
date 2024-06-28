print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)

priceSum = count = cheapestPrice = 0
cheapestName = ''

while True:
    name = str(input('Nome do Produto: '))
    price = float(input('Preço do Produto: '))

    if priceSum == 0:
        cheapestPrice = price

    priceSum += price

    if price > 1000:
        count += 1

    if cheapestPrice > price:
        cheapestPrice = price
        cheapestName = name

    option = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if option != 'S':
        break

print('--------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi R${priceSum:.2f}')
print(f'Temos {count} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {cheapestName} que custa R${cheapestPrice:.2f}')
