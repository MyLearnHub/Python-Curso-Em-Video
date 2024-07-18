def leiaDinheiro(value):
    while True:
        date = str(input(value)).replace(',', '.').strip()
        if date.isalpha() or date == '':
            print(f'\033[0;31mERRO: \"{date}\" é um preço inválido!\033[m')
        else:
            return float(date)
