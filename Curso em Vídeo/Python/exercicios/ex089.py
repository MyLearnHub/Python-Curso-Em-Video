students = list()


while True:
    student = list()
    notes = list()
    student.append(str(input('Nome: ')))
    notes.append(float(input('Nota 1: ')))
    notes.append(float(input('Nota 2: ')))

    student.append(notes[:])
    students.append(student[:])
    student.clear()
    notes.clear()

    continuation = str(input('Quer continuar? [S/N] '))
    if continuation in 'Nn':
        break

print('-=' * 30)
print('Nº NOME        MÉDIA')
print('-' * 30)
for key, student in enumerate(students):
    average = (student[1][0] + student[1][1]) / 2
    print(f'{key} {student[0]} {average:>10.1f}')
print('-' * 30)

while True:
    studentIndex = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if studentIndex == 999:
        break
    elif studentIndex >= len(students):
        print('Index inválido, tente novamente')
    else:
        print(f'Notas de {students[studentIndex][0]} são {students[studentIndex][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
