def count(* number):
    print(number)
    for value in number:
        print(f'{value} ', end='')
    print('FIM')
    size = len(number)
    print(f'Recebi os valores {number} e são ao todo {size} números')


count(2, 1, 7)
count(8, 0)
count(4, 4, 7, 6, 2)
