init = int(input('Primeiro termo: '))
ratio = int(input('Razão: '))

for count in range(10):
    tenth = init + count * ratio
    print('{} '.format(tenth), end='→ ')
print('ACABOU')

# Usando fórmula do décimo termo
'''
init = int(input('Primeiro termo: '))
ratio = int(input('Razão: '))
tenth = init + (10 - 1) * ratio

for count in range(init, tenth + ratio, ratio):
    print('{} '.format(count), end='→ ')
print('ACABOU')
'''
