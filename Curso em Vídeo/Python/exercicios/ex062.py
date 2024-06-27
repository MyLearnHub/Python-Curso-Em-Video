init = int(input('Primeiro termo: '))
ratio = int(input('Razão: '))
count = init
total = 10
terms = 1

while terms != 0:
    currentCount = 0
    while currentCount < total:
        print('{} '.format(count), end='→ ')
        count += ratio
        currentCount += 1
    print('ACABOU')
    terms = int(input('Quantos termos você quer mostrar a mais? (0 para parar): '))
    total = terms

print('Programa finalizado')
