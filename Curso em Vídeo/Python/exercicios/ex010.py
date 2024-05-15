real = float(input('Quanto real você tem na carteira? R$ '))
dolar = real / 5.13
euro = real / 5.55
iene = real / 0.033
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €${:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥${:.2f}'.format(real, iene))
