Algoritmo "fatorial"
Var
   i, value, factorial: inteiro
Inicio
   escreva("Qual número gostaria de saber o valor fatorial?")
   leia(value)
   
   i <- value
   factorial <- 1
   
   repita
      factorial <- factorial * i
      i <- i - 1
   ate (i < 1)
   
   escreva("Fatorial de", value, ":", factorial)
Fimalgoritmo