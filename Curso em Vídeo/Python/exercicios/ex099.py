from time import sleep


def maior(*valores):
    biggest = 0

    print('-=' * 30)
    print('Analisando os valores passados...')

    for value in valores:
        print(value, end=' ')
        sleep(0.3)
        if value > biggest:
            biggest = value

    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {biggest}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
