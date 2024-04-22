Algoritmo "par-ou-impar"
Var
   number: inteiro
Procedimento evenOrOdd(value: inteiro)
Inicio
   Se (value % 2 = 0) Entao
      Escreva("O número ", value, " é par")
   Senao
      Escreva("O número ", value, " é ímpar")
   FimSe
FimProcedimento
Inicio
   Escreva("Digite um número: ")
   Leia(number)
   evenOrOdd(number)
Fimalgoritmo