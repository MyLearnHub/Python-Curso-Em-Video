people = {'name': 'Gustavo', 'gender': 'M', 'age': 22}
print(people)
print(people['name'])
print(people['age'])
print(f'O {people["name"]} tem {people["age"]} anos')
print(people.keys())
print(people.values())
print(people.items())

for key in people.keys():
    print(key)

for value in people.values():
    print(value)

del people['gender']
people['name'] = 'Leandro'
people['weight'] = 98.5
for key, value in people.items():
    print(f'{key} = {value}')
