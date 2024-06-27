numberSum = count = higher = smallest = 0
response = 'S'

while response in 'Ss':
    number = int(input('Digite um valor:'))

    numberSum += number
    count += 1
    if count == 1:
        higher = smallest = number
    else:
        if number > higher:
            higher = number

        if number < smallest:
            smallest = number

    response = str(input('Quer continuar? [S / N]')).upper().strip()[0]

average = numberSum / count
print('Você digitou {} números e a média foi {}'.format(count, average))
print('O maior valor foi {} e o menor foi {}'.format(higher, smallest))
