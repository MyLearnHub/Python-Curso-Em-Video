def leiaInt(msg=''):
    while True:
        value = input(msg)

        if value.isnumeric():
            return value
        else:
            print('ERRO! Digite um número inteiro válido.')


print('-' * 30)
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
