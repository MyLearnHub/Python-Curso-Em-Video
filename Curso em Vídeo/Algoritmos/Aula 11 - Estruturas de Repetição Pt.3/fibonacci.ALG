Algoritmo "fibonacci"
Var
   i, current, last, next: inteiro
Inicio
   current <- 0
   last <- 1

   para i := 1 ate 15 faca
      escreva(current)
      next <- current + last
      last <- current
      current <- next
   fimpara
Fimalgoritmo