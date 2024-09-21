from uteis import numeros

number = int(input('Digite um valor: '))
fat = numeros.fatorial(number)
print(f'O fatorial de {number} é {fat}.')
print(f'O dobro de {number} é {numeros.dobro(number)}.')
