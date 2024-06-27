print('Gerador de PA')
print('-=' * 10)
init = int(input('Primeiro termo: '))
ratio = int(input('Razão da PA: '))
term = init
count = 1
total = 0
more = 10

while more != 0:
    total = total + more
    while count <= total:
        print('{} '.format(term), end='→ ')
        term += ratio
        count += 1
    print('PAUSA')
    more = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
