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
