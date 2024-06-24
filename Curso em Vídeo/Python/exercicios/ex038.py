numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('O primeiro número é maior que o segundo')
elif numero2 > numero1:
    print('O segundo número é maior que o primeiro')
else:
    print('Não existe valor maior, os dois são iguais')
