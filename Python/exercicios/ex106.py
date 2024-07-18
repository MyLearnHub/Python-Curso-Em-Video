from time import sleep

colors = ('\033[m',
          '\033[0;30;41m',
          '\033[0;30;42m',
          '\033[0;30;43m',
          '\033[0;30;44m',
          '\033[0;30;45m',
          '\033[7;30')


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(colors[6], end='')
    help(comando)
    print(colors[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(colors[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(colors[0], end='')
    sleep(1)


comand = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comand = str(input('Função ou Biblioteca > '))
    if comand.strip().upper() == 'FIM':
        break
    else:
        ajuda(comand)

titulo('ATÉ LOGO!', 1)
