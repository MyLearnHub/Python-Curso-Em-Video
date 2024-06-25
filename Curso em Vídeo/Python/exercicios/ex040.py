firstGrade = float(input('Primeira nota: '))
secondGrade = float(input('Segunda nota: '))

average = (firstGrade + secondGrade) / 2
situation = ""

print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(firstGrade, secondGrade, average))
if 7 > average >= 5:
    situation = 'em RECUPERAÇÂO'
elif average < 5:
    situation = 'REPROVADO'
else:
    situation = 'APROVADO'

print("O aluno está {}.".format(situation))
