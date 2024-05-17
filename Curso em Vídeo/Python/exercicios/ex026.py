frase = str(input('Digite uma frase: '))
print('Letras A na frase: {}'.format(frase.lower().count('a')))
print('Posição da primeira letra A na frase: {}'.format(frase.strip().lower().find('a')))
print('Posição da última letra A na frase: {}'.format(frase.strip().lower().rfind('a')))
