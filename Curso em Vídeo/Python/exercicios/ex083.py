expression = input('Digite a expressão: ')

stack = []

for char in expression:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(char)

if len(stack) == 0:
    print('Sua expressão está válida!')
else:
    print('A expressão está errada!')
