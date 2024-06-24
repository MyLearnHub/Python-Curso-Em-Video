from random import choice
ppt = str(input('Jogue um valor (Pedra, Papel, Tesoura): '))

elementos = ['Pedra', 'Papel', 'Tesoura']
escolhido = choice(elementos)

if ppt == escolhido:
    print("Empate")
elif ppt == 'Tesoura' and escolhido == 'Papel' or ppt == 'Papel' and escolhido == 'Pedra' or ppt == 'Pedra' and escolhido == 'Tesoura':
    print('Você ganhou')
else:
    print('Você perdeu')

print('Você jogou {}'.format(ppt))
print('A máquina jogou {}'.format(escolhido))
