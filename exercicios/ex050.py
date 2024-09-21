numberSum = 0
count = 0
for turn in range(1, 7):
    number = int(input('Digite o {}º valor: '.format(turn)))

    if number % 2 == 0:
        numberSum += number
        count += 1

print('Você informou {} números PARES e a soma foi {}'.format(count, numberSum))
