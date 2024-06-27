number = 0
numberSum = 0
higher = 0
smallest = 0
continuation = 'S'
count = 0

while continuation == 'S':
    number = int(input('Digite um valor:'))
    if count == 0:
        higher = number
        smallest = number

    numberSum += number
    if number > higher:
        higher = number

    if number < smallest:
        smallest = number

    count += 1
    average = numberSum / count
    print('Você digitou {} números, que somados são {}'.format(count, numberSum))

    continuation = str(input('Quer continuar? [S / N]')).upper()
print('Saindo...')