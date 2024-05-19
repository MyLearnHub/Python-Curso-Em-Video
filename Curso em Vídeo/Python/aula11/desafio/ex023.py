number = int(input('Informe um número: '))

unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousands = number // 1000 % 10

print('Analisando o número {}'.format(number))
print('Unidade: {}'.format(unit))
print('Deneza: {}'.format(ten))
print('Centena: {}'.format(hundred))
print('Milhar: {}'.format(thousands))
