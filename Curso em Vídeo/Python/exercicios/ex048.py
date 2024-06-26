numberSum = 0
for number in range(1, 501, 2):
    if number % 3 == 0:
        numberSum += number

print('Soma: {}'.format(numberSum))

# Validando se é ímpar
'''
for number in range(1, 501, 2):
    if number % 2 == 1 and number % 3 == 0:
        numberSum += number
'''