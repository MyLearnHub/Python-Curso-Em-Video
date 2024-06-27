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
    continuation = str(input('Quer continuar? [S / N]')).upper()

average = numberSum / count
print('Média dos valores: {}'.format(average))
print('Maior valor: {}'.format(higher))
print('Menor valor: {}'.format(smallest))
