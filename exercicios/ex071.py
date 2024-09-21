print('=' * 30)
print(f'{'BANCO CEV':^30}')
print('=' * 30)
number = int(input('Que valor você quer sacar? R$ '))
withdraw = number
bill = 50
totalBill = 0

while True:
    if withdraw >= bill:
        withdraw -= bill
        totalBill += 1
    else:
        if totalBill > 0:
            print(f'Total de {totalBill} cédulas de R${bill}')

        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1

        totalBill = 0

        if withdraw == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

# Múltiplos While
'''
print('=' * 30)
print(f'{'BANCO CEV':^30}')
print('=' * 30)
number = int(input('Que valor você quer sacar? R$ '))
fifty = twenty = ten = one = 0
value = 0

while True:
    if value + 50 > number:
        if fifty != 0:
            print(f'Total de {fifty} cédulas de R$50')
        break
    else:
        value += 50
        fifty += 1

while True:
    if value + 20 > number:
        if twenty != 0:
            print(f'Total de {twenty} cédulas de R$20')
        break
    else:
        value += 20
        twenty += 1

while True:
    if value + 10 > number:
        if ten != 0:
            print(f'Total de {ten} cédulas de R$10')
        break
    else:
        value += 10
        ten += 1

while True:
    if value + 1 > number:
        if one != 0:
            print(f'Total de {one} cédulas de R$1')
        break
    else:
        value += 1
        one += 1

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
