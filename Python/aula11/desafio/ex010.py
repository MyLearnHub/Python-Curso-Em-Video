real = float(input('\033[1;36;40mQuanto real você tem na carteira? R$ \033[m'))

dolar = real / 5.13
euro = real / 5.55
iene = real / 0.033

print('\033[1;33mCom R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €${:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥${:.2f}'.format(real, iene))
