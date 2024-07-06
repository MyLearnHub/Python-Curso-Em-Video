def contador(init, end, step):
    """
    -> Faz uma contagem e mostra na tela.
    :param init: início da contagem
    :param end: fim da contagem
    :param step: passo da contagem
    :return: sem retorno
    """
    count = init
    while count <= end:
        print(f'{count}', end='')
        count += step
    print('FIM!')


contador(0, 100, 10)
help(contador)
