# n1 = input('Digite um valor: ')
# print(type(n1))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale', s) # Concatenando
print('A soma entre {} e {} vale {}'.format(n1, n2, s))  # Formatando
