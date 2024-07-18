number = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:')
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
option = int(input('Sua opção: '))

if option != 1 or option != 2 or option != 3:
    print('Opção inválida. Tente novamente.')
else:
    if option == 1:
        base = 'BINÁRIO'
        convertedNumber = bin(number)
    elif option == 2:
        base = 'OCTAL'
        convertedNumber = oct(number)
    elif option == 3:
        base = 'HEXADECIMAL'
        convertedNumber = hex(number)

    print('{} convertido para {} é igual a {}'.format(number, base, convertedNumber[2:]))
