name = 'José'
age = 33
wage = 987.35
print(f'O {name:^20} tem {age} anos e ganha R${wage:.2f}.')  # Python 3.6+
print(f'O {name:-^20} tem {age} anos e ganha R${wage:.2f}.')
print(f'O {name:->20} tem {age} anos e ganha R${wage:.2f}.')
print(f'O {name:-<20} tem {age} anos e ganha R${wage:.2f}.')
print('O {:^20} tem {} anos e ganha R${:.2f}.'.format(name, age, wage))  # Python 3
print('O {:-^20} tem {} anos e ganha R${:.2f}.'.format(name, age, wage))
print('O {:->20} tem {} anos e ganha R${:.2f}.'.format(name, age, wage))
print('O {:-<20} tem {} anos e ganha R${:.2f}.'.format(name, age, wage))
print('O %s tem %d anos e ganha R$%d' % (name, age, wage))  # Python 2
