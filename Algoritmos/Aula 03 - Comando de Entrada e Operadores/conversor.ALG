Algoritmo "conversor"
  Var
    angle, seno: real
  Inicio
    escreva("Informe um ângulo:")
    leia(angle)
    seno <- sen(grauprad(angle))
    escreva("O seno de", angle, " é:", seno)
Fimalgoritmo