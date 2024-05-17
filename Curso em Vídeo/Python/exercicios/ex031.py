distancia = float(input('Diga a distância da viagem (km): '))
if distancia <= 200:
    distancia = distancia * 0.50
else:
    distancia = distancia * 0.45
print('Preço final: R${}'.format(distancia))
