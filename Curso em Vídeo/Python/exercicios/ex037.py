numero = int(input('Digite um número qualquer'))
print('O que você quer fazer com esse número?')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input())

base = ""
numeroConvertido = 0

if opcao == 1:
    base = 'Binário'
    numeroConvertido = bin(numero)
elif opcao == 2:
    base = 'Octal'
    numeroConvertido = oct(numero)
else:
    base = 'Hexadecimal'
    numeroConvertido = hex(numero)

print('O {} na base {} é {}'.format(numero, base, numeroConvertido))
