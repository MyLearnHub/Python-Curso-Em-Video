print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
number = int(input('Quantos termos você quer mostrar? '))
firstTerm = 0
secondTerm = 1

print('~' * 30)
print('{} → {}'.format(firstTerm, secondTerm), end='')
cont = 3
while cont <= number:
    thirdTerm = firstTerm + secondTerm
    print(' → {}'.format(thirdTerm), end='')
    firstTerm = secondTerm
    secondTerm = thirdTerm
    cont += 1

print(' → FIM')
print('~' * 30)
