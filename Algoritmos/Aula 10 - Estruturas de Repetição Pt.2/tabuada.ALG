Algoritmo "tabuada"
Var
   i, number, result: inteiro
Inicio
   i <- 1

   escreva("Gostaria de saber a tabuada de qual número?")
   leia(number)

   repita
      result <- number * i
      escreval(number, " x", i, " =", result)
      i <- i + 1
   ate (i > 10)
Fimalgoritmo