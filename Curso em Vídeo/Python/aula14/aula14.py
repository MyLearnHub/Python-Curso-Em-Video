number = 1
even = odd = 0

while number != 0:
    number = int(input('Digite um valor: '))
    if number != 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
print('Você digitou {} números pares e {} números ímpares'.format(even, odd))
