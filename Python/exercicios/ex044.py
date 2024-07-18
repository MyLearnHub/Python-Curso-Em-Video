print('{:=^40}'.format(' LOJAS GUANABARA '))
price = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é a opção? '))

if option < 1 or option > 4:
    print('OPÇÂO INVÁLIDA de pagamento. Tente novamente!')
else:
    if option == 1:
        newPrice = price * 0.90
    elif option == 2:
        newPrice = price * 0.95
    elif option == 3:
        newPrice = price
        installmentValue = newPrice / 2

        print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(installmentValue))
    else:
        installments = int(input('Quantas parcelas? '))

        newPrice = price * 1.20
        installmentValue = newPrice / installments

        print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(installments, installmentValue))

    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, newPrice))
