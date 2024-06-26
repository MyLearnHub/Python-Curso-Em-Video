number = int(input('Digite um número: '))
aux = 0

for divisor in range(1, number + 1):
    if number % divisor == 0:
        aux += 1

if aux == 2 or number == 1:
    print('{} é primo'.format(number))
else:
    print('{} não é primo'.format(number))
