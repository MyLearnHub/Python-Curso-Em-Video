def leiaInt(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return number


def leiaFloat(msg):
    while True:
        try:
            number = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return number


print('-' * 30)
integer = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {integer} e o real foi {real}')
