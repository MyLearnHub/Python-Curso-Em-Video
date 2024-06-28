while True:
    number = int(input('Quer ver a tabuada de qual valor? '))

    print('-' * 30)
    if number < 0:
        break

    for count in range(1, 11):
        print(f'{number} x {count:2} = {number * count}')
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
