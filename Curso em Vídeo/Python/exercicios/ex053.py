phrase = input("Digite uma frase: ").upper().replace(" ", "")

palindromo = True
size = len(phrase)

for i in range(size // 2):
    if phrase[i] != phrase[size - i - 1]:
        palindromo = False

if palindromo:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
