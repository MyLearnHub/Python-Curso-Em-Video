def aumentar(price, percentage, formatar=False):
    price += (price * percentage / 100)

    if formatar:
        return f'R${price:.2f}'.replace('.', ',')

    return price


def diminuir(price, percentage, formatar=False):
    price -= (price * percentage / 100)

    if formatar:
        return f'R${price:.2f}'.replace('.', ',')

    return price


def dobro(price, formatar=False):
    price *= 2

    if formatar:
        return f'R${price:.2f}'.replace('.', ',')

    return price


def metade(price, formatar=False):
    price /= 2

    if formatar:
        return f'R${price:.2f}'.replace('.', ',')

    return price


def moeda(price):
    return f'R${price:.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco):>11}')
    print(f'Dobro do preço: {dobro(preco, True):>11}')
    print(f'Metade do preço: {metade(preco, True):>11}')
    print(f'{aumento}% de aumento: {aumentar(preco, aumento, True):>11}')
    print(f'{reducao}$ de redução: {diminuir(preco, reducao, True):>11}')
    print('-' * 30)
