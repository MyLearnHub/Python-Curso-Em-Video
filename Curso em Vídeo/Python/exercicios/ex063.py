number = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))

if number > 0:
    sequence = []
    a, b = 0, 1
    for _ in range(number):
        sequence.append(a)
        a, b = b, a + b

    print(' → '.join(map(str, sequence)) + ' → ACABOU')
else:
    print('Por favor, insira um número positivo.')
