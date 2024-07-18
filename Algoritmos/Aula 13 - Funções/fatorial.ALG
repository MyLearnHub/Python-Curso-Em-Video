Algoritmo "fatorial"
Var
   number, result: inteiro
   
Funcao factorial(value: inteiro): inteiro
Var
   i, result: inteiro
Inicio
   result <- 1
   para i <- 1 ate value faca
      result <- result * i
   fimpara
   
   retorne result
FimFuncao

Inicio
   escreva("Digite um número: ")
   leia(number)
   
   result <- factorial(number)
   
   escreva("O valor de", number, "! é igual a", result)
Fimalgoritmo