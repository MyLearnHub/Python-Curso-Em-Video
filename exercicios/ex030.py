number = int(input('Me diga um número qualquer: '))

result = number % 2

if result == 0:
    print('O número {} é PAR'.format(number))
else:
    print('O número {} é ÍMPAR'.format(number))
