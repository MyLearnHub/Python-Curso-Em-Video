largura = float(input('Digite a largura da parede (m): '))
altura = float(input('Digite a altura da parede (m): '))
area = largura * altura
tinta = area / 2
print('Você precisa de {} litros de tinta para {}m2'.format(tinta, area))
