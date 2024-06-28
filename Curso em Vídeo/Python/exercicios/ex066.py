count = numberSum = 0
while True:
    number = int(input('Digite um valor (999 para parar): '))

    if number == 999:
        break

    numberSum += number
    count += 1

print(f'A soma dos {count} valores foi {numberSum}!')
