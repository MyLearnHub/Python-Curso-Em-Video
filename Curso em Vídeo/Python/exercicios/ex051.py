init = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for count in range(10):
    termo = init + count * razao
    print(termo)
