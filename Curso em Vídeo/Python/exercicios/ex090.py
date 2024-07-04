name = str(input('Nome: '))
average = float(input(f'Média de {name}: '))
situation = 'Aprovado' if average >= 6 else 'Reprovado'
student = {'Nome': name, 'Média': average, 'Situação': situation}

for key, value in student.items():
    print(f'{key} é igual a {value}')
