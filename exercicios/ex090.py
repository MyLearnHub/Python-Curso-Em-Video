student = dict()
student['nome'] = str(input('Nome: '))
student['média'] = float(input(f'Média de {student['nome']}: '))
student['situação'] = 'Aprovado'
if 5 <= student['média'] < 7:
    student['situação'] = 'Recuperação'
else:
    student['situação'] = 'Reprovado'

print('-=' * 30)
for key, value in student.items():
    print(f' - {key} é igual a {value}')
