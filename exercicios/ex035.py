print('-=' * 20)
print('Analisador de triângulo')
print('-=' * 20)
straight1 = float(input('Primeiro segmento: '))
straight2 = float(input('Segundo segmento: '))
straight3 = float(input('Terceiro segmento: '))

if straight1 < straight2 + straight3 and straight2 < straight1 + straight3 and straight3 < straight1 + straight2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
