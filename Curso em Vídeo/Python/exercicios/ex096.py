def area(largura, comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura * comprimento}m².')


print('Controle de terrenos')
print('-' * 20)
width = float(input('LARGURA (m): '))
length = float(input('COMPRIMENTO (m): '))
area(width, length)
