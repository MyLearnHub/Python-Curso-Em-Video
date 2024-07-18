from time import sleep

firstNumber = int(input('Primeiro valor: '))
secondNumber = int(input('Segundo valor: '))
option = 0

while option != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    option = int(input('>>>>> Qual é a sua opção: '))

    if option == 1:
        numberSum = firstNumber + secondNumber
        print('A soma entre {} + {} é: {}'.format(firstNumber, secondNumber, numberSum))
    elif option == 2:
        numberMultiplication = firstNumber * secondNumber
        print('A resultado de {} x {} é {}'.format(firstNumber, secondNumber, numberMultiplication))
    elif option == 3:
        if firstNumber > secondNumber:
            print('Entre {} e {} o maior valor é {}'.format(firstNumber, secondNumber, firstNumber))
        else:
            print('Entre {} e {} o maior valor é {}'.format(secondNumber, firstNumber, secondNumber))
    elif option == 4:
        print('Informe os números novamente:')
        firstNumber = int(input('Primeiro valor: '))
        secondNumber = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
