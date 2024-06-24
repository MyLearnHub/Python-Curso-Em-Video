straight1 = float(input('Primeiro segmento: '))
straight2 = float(input('Segundo segmento: '))
straight3 = float(input('Terceiro segmento: '))
tipoTriangulo = ''

if straight1 < straight2 + straight3 and straight2 < straight1 + straight3 and straight3 < straight1 + straight2:
    if straight1 == straight2 == straight3:
        tipoTriangulo = 'EQUILÁTERO'
    elif straight1 == straight2 or straight2 == straight3 or straight3 == straight1:
        tipoTriangulo = 'ISÓSCELES'
    else:
        tipoTriangulo = 'ESCALENO'

    print('Os segmentos acima PODEM FORMAR um triângulo {}'.format(tipoTriangulo))
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')