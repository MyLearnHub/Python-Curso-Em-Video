straight1 = float(input('Primeiro segmento: '))
straight2 = float(input('Segundo segmento: '))
straight3 = float(input('Terceiro segmento: '))

if straight1 < straight2 + straight3 and straight2 < straight1 + straight3 and straight3 < straight1 + straight2:
    if straight1 == straight2 == straight3:
        triangleType = 'EQUILÁTERO'
    elif straight1 != straight2 != straight3 != straight1:
        triangleType = 'ESCALENO'
    else:
        triangleType = 'ISÓSCELES'

    print('Os segmentos acima PODEM FORMAR um triângulo {}!'.format(triangleType))
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
