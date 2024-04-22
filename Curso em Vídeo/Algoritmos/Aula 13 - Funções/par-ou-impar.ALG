Algoritmo "par-ou-impar"
Var
   number: inteiro
   result: caractere

Funcao evenOrOdd(value: inteiro): caractere
Inicio
   se (value % 2 = 0) entao
      retorne "par"
   senao
      retorne "ímpar"
   fimse
FimFuncao

Inicio
   escreval("Vamos descobrir se um número é par ou ímpar")
   escreva("Digite um número: ")
   leia(number)
   
   result <- evenOrOdd(number)
   
   escreva("O número", number, " é ", result)
Fimalgoritmo