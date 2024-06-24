preco = float(input('Preço do produto: R$'))
print('Digite a condição do pagamento:')
print('[1] - Á vista em Dinheiro / Cheque')
print('[2] - Á vista no Cartão')
print('[3] - Até 2x no Cartão')
print('[4] - 3x ou mais no Cartão')
condicao = int(input())

if condicao == 1:
    preco = preco * 0.90
elif condicao == 2:
    preco = preco * 0.95
elif condicao == 4:
    preco = preco * 1.20

print('Valor final a pagar: {}'.format(preco))
