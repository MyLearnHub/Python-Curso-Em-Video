words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar',  'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for position, letter in enumerate(words):
    print(f'Na palavra {letter.upper()}', end=' ')
    print('temos ', end='')
    if 'a' in words[position]:
        print('a', end='')

    if 'e' in words[position]:
        print('e', end='')

    if 'i' in words[position]:
        print('i', end='')

    if 'o' in words[position]:
        print('o', end='')

    if 'u' in words[position]:
        print('u', end='')
    print('')
