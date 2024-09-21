numbers = [2, 5, 9, 1]
numbers[2] = 3
numbers.append(7)  # Adiciona a lista
numbers.sort(reverse=True)  # Ordena a lista ao contrário
numbers.insert(2, 0)  # Adiciona o 0 no 2º Index
numbers.pop()  # Remove o último elemento
numbers.pop(2)  # Remove o elemento no 2º Index
numbers.remove(2)  # Remove o primeiro valor 2 encontrado

if 4 in numbers:
    numbers.remove(4)  # Remove o primeiro valor 4 encontrado se existir
else:
    print('Não achei o número 4')
    
print(numbers)
print(f'Essa lista tem {len(numbers)} elementos')
