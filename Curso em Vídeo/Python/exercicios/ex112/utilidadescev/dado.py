def leiaDinheiro(value):
    while True:
        date = input(value).strip().replace(',', '.')
        if date.isnumeric() or date.isdecimal():
            return float(date)
        else:
            print(f'ERRO: "{date}" é um preço inválido!')
