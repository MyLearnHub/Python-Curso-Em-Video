nome = str(input('Qual o seu nome? '))
print('Prazer em te conhecer {:20}!'.format(nome))  # Entende como um espaçamento de 20 caracteres

nome = str(input('Qual o seu nome? '))
print('Prazer em te conhecer {:>20}!'.format(nome))  # Alinha a direita do espaçamento

nome = str(input('Qual o seu nome? '))
print('Prazer em te conhecer {:<20}!'.format(nome))  # Alinha a esquerda do espaçamento

nome = str(input('Qual o seu nome? '))
print('Prazer em te conhecer {:^20}!'.format(nome))  # Alinha ao meio do espaçamento

nome = str(input('Qual o seu nome? '))
print('Prazer em te conhecer {:=^20}!'.format(nome))  # Adiciona o caractere '=' no espaço restante