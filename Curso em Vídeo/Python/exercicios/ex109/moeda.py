def aumentar(price, percentage, formatar=False):
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
