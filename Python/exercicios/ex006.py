number = int(input('Digite um número: '))

double = number * 2
triple = number * 3
squareRoot = number ** 0.5
# squareRoot = pow(number, 0.5) # Raiz Quadrada Alternativa. Também pode ser "1 / 2" ao invés de 0.5

print('O dobro de {} vale {}.'.format(number, double))
print('O triplo de {} vale {}.'.format(number, triple))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(number, squareRoot))

