from time import sleep


def fatorial(number, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param number: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número number.
    """

    fatorial_count = 1
    for count in range(number, 0, -1):
        if show:
            print(count, end='')
            sleep(0.3)
            if count > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial_count *= count

    return fatorial_count


print('-' * 30)
print(fatorial(5))
help(fatorial)