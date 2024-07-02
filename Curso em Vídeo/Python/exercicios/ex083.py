expression = input('Digite a expressão: ')

stack = []

for caracter in expression:
    if caracter == '(':
        stack.append('(')
    elif caracter == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')

if len(stack) == 0:
    print('Sua expressão está válida!')
else:
    print('A expressão está errada!')
