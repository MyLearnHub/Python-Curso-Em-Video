option = 0
firstNumber = int(input('Primeiro valor: '))
secondNumber = int(input('Segundo valor: '))

while option != 5:
    print('''Escolha uma opção:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior Valor
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    option = int(input('Opção: '))

    if option == 1:
        numberSum = firstNumber + secondNumber
        print('A soma entre os valores é: {}'.format(numberSum))
    elif option == 2:
        numberMultiplication = firstNumber * secondNumber
        print('A multiplicação entre os valores é: {}'.format(numberMultiplication))
    elif option == 3:
        if firstNumber > secondNumber:
            print('{} é maior que {}'.format(firstNumber, secondNumber))
        else:
            print('{} é maior que {}'.format(secondNumber, firstNumber))
    elif option == 4:
        firstNumber = int(input('Primeiro valor: '))
        secondNumber = int(input('Segundo valor: '))
    else:
        print('Saindo...')
