def aumentar(price, percentage):
    price = price + (price * percentage / 100)
    return price


def diminuir(price, percentage):
    price = price - (price * percentage / 100)
    return price


def dobro(price):
    price *= 2
    return price


def metade(price):
    price /= 2
    return price
