init = int(input('Primeiro termo: '))
ratio = int(input('Razão: '))
tenth = init + (10 - 1) * ratio
count = init

while count <= tenth:
    print('{} '.format(count), end='→ ')
    count += ratio
print('ACABOU')
