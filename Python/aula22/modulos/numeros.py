import uteis
# from uteis import fatorial, dobro

number = int(input('Digite um valor: '))
fat = uteis.fatorial(number)
print(f'O fatorial de {number} é {fat}.')
print(f'O dobro de {number} é {uteis.dobro(number)}.')
