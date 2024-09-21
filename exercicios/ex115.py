from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

file = 'cursoemvideo.txt'

if not fileExists(file):
    criarArquivo(file)

while True:
    response = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if response == 1:
        lerArquivo(file)
    elif response == 2:
        header('NOVO CADASTRO')
        name = str(input('Nome: '))
        age = leiaInt('Idade: ')
        sign_up(file, name, age)
    elif response == 3:
        header('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
