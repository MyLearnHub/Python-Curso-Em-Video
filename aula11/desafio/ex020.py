from random import shuffle

student1 = str(input('\033[1;31;40mPrimeiro aluno: '))
student2 = str(input('Segundo aluno: '))
student3 = str(input('Terceiro aluno: '))
student4 = str(input('Quarto aluno: '))

list = [student1, student2, student3, student4]
shuffle(list)

print('A ordem de apresentação será\n {}'.format(list))
