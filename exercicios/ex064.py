number = count = numberSum = 0

while number != 999:
    number = int(input('Digite um número [999 para parar]: '))
    if number != 999:
        numberSum += number
        count += 1
print('Você digitou {} númerose a soma entre eles foi {}'.format(count, numberSum))

# Sem validação
'''
number = count = numberSum = 0
number = int(input('Digite um número [999 para parar]: '))

while number != 999:
    numberSum += number
    count += 1
    number = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} númerose a soma entre eles foi {}'.format(count, numberSum))
'''