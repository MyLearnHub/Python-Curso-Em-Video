students = list()

while True:
    name = str(input('Nome: '))
    firstNote = float(input('Nota 1: '))
    secondNote = float(input('Nota 2: '))
    average = (firstNote + secondNote) / 2
    students.append([name, [firstNote, secondNote], average])

    continuation = str(input('Quer continuar? [S/N] '))
    if continuation in 'Nn':
        break

print('-=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 26)
for key, student in enumerate(students):
    print(f'{key:<4}{student[0]:<10}{student[2]:>8.1f}')
print('-' * 30)

while True:
    print('-' * 35)
    studentIndex = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if studentIndex == 999:
        print('FINALIZANDO...')
        break
    elif studentIndex >= len(students):
        print('Index inválido, tente novamente')
    else:
        print(f'Notas de {students[studentIndex][0]} são {students[studentIndex][1]}')
print('<<< VOLTE SEMPRE >>>')
