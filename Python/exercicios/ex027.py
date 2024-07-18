treatedName = str(input('Digite seu nome completo: ')).strip()

name = treatedName.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu último nome é {}'.format(name[len(name) - 1]))

"""name = str(input('Digite seu nome completo: ')).split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu último nome é {}'.format(name[-1]))"""  # Alternativa
