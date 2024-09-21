guys = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(guys)
print(guys[0])
print(guys[0][0])
print(guys[2][1])

for person in guys:
    print(person)
    print(person[0])
    print(person[1])
    print(f'{person[0]} tem {person[1]} anos de idade.')