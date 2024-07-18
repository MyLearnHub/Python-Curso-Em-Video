measure = float(input('Uma distância em metros: '))

km = measure / 1000
hm = measure / 100
dam = measure / 10
dm = measure * 10
cm = measure * 100
mm = measure * 1000

print('A medida de {}m corresponde a'.format(measure))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
