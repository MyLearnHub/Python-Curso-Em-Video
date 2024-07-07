def voto(birthYear):
    from datetime import date

    age = date.today().year - birthYear

    if age < 16:
        status = "NÃO VOTA"
    elif 16 <= age < 18 or age >= 65:
        status = "VOTO OPCIONAL"
    else:
        status = "VOTO OBRIGATÓRIO"

    return f'Com {age} anos: {status}.'


print('-' * 30)
year = int(input('Em que ano você nasceu? '))
print(voto(year))
