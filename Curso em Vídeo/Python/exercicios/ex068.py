from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
count = 0

while True:
    playerNumber = int(input('Digite um valor: '))
    playerChoice = ' '
    while playerChoice not in 'PpIi':
        playerChoice = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computerNumber = randint(0, 11)

    numberSum = playerNumber + computerNumber
    evenOdd = 'PAR' if numberSum % 2 == 0 else 'ÍMPAR'

    print('-' * 30)
    print(f'Você jogou {playerNumber} e o computador {computerNumber}. Total de {numberSum} DEU {evenOdd}!')
    print('-' * 30)
    if evenOdd == 'PAR' and playerChoice == 'P' or evenOdd == 'ÍMPAR' and playerChoice == 'I':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        count += 1
    else:
        print('Você PERDEU!')
        break

print('=-' * 15)
print(f'GAME OVER! Você venceu {count} vezes.')
