Algoritmo "fibonacci"
Var
   i, current, last, next: inteiro
   
Procedimento fibonacci(Var value1, value2: inteiro)
Var
   value3: inteiro
Inicio
   value3 <- value1 + value2
   escreval(value3)
   value1 <- value2
   value2 <- value3
FimProcedimento

Inicio
   current <- 0
   escreval(current)
   last <- 1
   escreval(last)
   
   para i <- 0 ate 12 faca
      fibonacci(current, last)
   fimpara
Fimalgoritmo