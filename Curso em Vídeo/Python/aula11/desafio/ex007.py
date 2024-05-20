number1 = float(input('\033[1;32;47mPrimeira nota do aluno: '))
number2 = float(input('Segunda nota do aluno: \033[m'))

average = (number1 + number2) / 2

print('\033[1;30;41mA média entre {:.1f} e {:.1f} é igual a {:.1f}\033[m'.format(number1, number2, average))
