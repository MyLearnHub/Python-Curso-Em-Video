from random import sample

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
ordem = sample([nome1, nome2, nome3, nome4], k=4)
print('O aluno escolhido foi: {}'.format(ordem))
