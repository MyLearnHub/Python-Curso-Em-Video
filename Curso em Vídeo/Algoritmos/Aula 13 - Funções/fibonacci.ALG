Algoritmo "fibonacci"
Var
   i, current, last, next: inteiro

Funcao fibonacci(Var value1, value2: inteiro): inteiro
Var
   value3: inteiro
Inicio
   value3 <- value1 + value2
   value1 <- value2
   value2 <- value3
   retorne(value3)
FimFuncao

Inicio
   current <- 0
   escreva(current)
   last <- 1
   escreva(last)

   para i <- 0 ate 12 faca
      next <- fibonacci(current, last)
      escreva(next)
   fimpara
Fimalgoritmo