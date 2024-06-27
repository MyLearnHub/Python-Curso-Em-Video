number = 0
numberSum = 0
count = 0

while number != 999:
    number = int(input('Digite um valor:'))
    if number != 999:
        numberSum += number
        count += 1
print('Você digitou {} números, que somados são {}'.format(count, numberSum))
