def leiaInt(msg=''):
    while True:
        value = input(msg)

        if value.isnumeric():
            return value
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


print('-' * 30)
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
