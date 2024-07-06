def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e retorna o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Paulo Alvares para o Curso em Vídeo.
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 2)
somar(3)
somar()
somar(b=4, c=2)
somar(c=3, a=2)
