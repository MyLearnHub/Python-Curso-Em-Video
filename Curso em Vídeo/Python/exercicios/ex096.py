def area(largura, comprimento):
    calculate = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {calculate}m².')


print('Controle de Terrenos')
print('-' * 20)
width = float(input('LARGURA (m): '))
length = float(input('COMPRIMENTO (m): '))
area(width, length)
