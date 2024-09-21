def aumentar(price, percentage, formatar=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param price: o preço que se quer reajustar
    :param percentage: qual é a porcentagem do aumento.
    :param formatar: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    price += (price * percentage / 100)
    return price if formatar is False else moeda(price)


def diminuir(price, percentage, formatar=False):
    price -= (price * percentage / 100)
    return price if formatar is False else moeda(price)


def dobro(price, formatar=False):
    price *= 2
    return price if formatar is False else moeda(price)


def metade(price, formatar=False):
    price /= 2
    return price if formatar is False else moeda(price)


def moeda(price):
    return f'R${price:.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
