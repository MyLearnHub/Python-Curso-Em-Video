number = int(input('Digite um número: '))
total = 0

for divider in range(1, number + 1):
    if number % divider == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(divider), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(number, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
