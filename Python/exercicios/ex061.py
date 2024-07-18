print('Gerador de PA')
print('-=' * 10)
init = int(input('Primeiro termo: '))
ratio = int(input('Razão da PA: '))
term = init
count = 1

while count <= 10:
    print('{} '.format(term), end='→ ')
    term += ratio
    count += 1
print('FIM')
