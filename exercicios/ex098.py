from time import sleep


def contador(init, end, step):
    if step < 0:
        step *= -1

    if step == 0:
        step = 1

    print('-=' * 20)
    print(f'Contagem de {init} até {end} de {step} em {step}')
    sleep(2.5)

    if init < end:
        count = init
        while count <= end:
            print(count, end=' ')
            sleep(0.5)
            count += step
        print('FIM!')
    else:
        count = init
        while count >= end:
            print(count, end=' ')
            sleep(0.5)
            count -= step
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
