phrase = input("Digite uma frase: ").upper().replace(" ", "")
palindrome = True
size = len(phrase)

for word in range(size // 2):
    if phrase[word] != phrase[size - word - 1]:
        palindrome = False

if palindrome:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")

# Usando formatação de Strings
'''
phrase = input("Digite uma frase: ").strip().upper()
words = phrase.split()
concatenation = ''.join(words)
reverse = ''

for word in range(len(concatenation) - 1, -1, -1):
    reverse += concatenation[word]

print('O inverso de {} é {}'.format(concatenation, reverse))
if reverse == concatenation:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
'''

# Sem usar for
'''
phrase = input("Digite uma frase: ").strip().upper()
words = phrase.split()
concatenation = ''.join(words)
reverse = concatenation[::-1]

print('O inverso de {} é {}'.format(concatenation, reverse))
if reverse == concatenation:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
'''
