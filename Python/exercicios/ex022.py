name = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúsculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
# print('Seu nome tem ao todo {} letras'.format(len(nome.replace(" ", ""))))  #  Alternativa
separator = name.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separator[0], len(separator[0])))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
