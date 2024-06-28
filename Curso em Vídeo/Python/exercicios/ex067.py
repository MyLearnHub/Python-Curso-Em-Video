number = count = 1

while True:
    number = int(input('Quer ver a tabuada de qual valor? '))

    if number < 0:
        break

    print('-' * 30)
    while count <= 10:
        print('{} x {:2} = {}'.format(number, count, number * count))
        count += 1
    print('-' * 30)
    count = 1

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
