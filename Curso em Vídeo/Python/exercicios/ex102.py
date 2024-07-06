from time import sleep


def fatorial(number, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param number: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número number.
    """

    fatorialCount = 1
    for count in range(number, 0, -1):
        if show:
            print(f'{count} x', end=' ')
            sleep(0.3)
        fatorialCount *= count
    print('=', end=' ')

    return fatorialCount


print('-' * 30)
print(fatorial(5, True))
