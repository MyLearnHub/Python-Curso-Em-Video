num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = 0
menor = 0
if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        menor = num3
    else:
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        menor = num3
    else:
        menor = num1
else:
    maior = num3
    if num1 > num2:
        menor = num2
    else:
        menor = num1
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
