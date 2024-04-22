Algoritmo "soma-com-escopo"
Var
   number1, number2: inteiro
   
Procedimento sum(var value1, value2: inteiro)
Inicio
   value1 <- value1 + 1
   value2 <- value2 + 2
   
   escreval("valor de value1: ", value1)
   escreval("valor de value2: ", value2)
   escreval("A soma vale: ", value1 + value2)
FimProcedimento

Inicio
   escreva("Digite um número:")
   leia(number1)
   escreva("Digite outro número:")
   leia(number2)
   
   sum(number1, number2)
   
   escreval("Valor de number1: ", number1)
   escreval("Valor de number2: ", number2)
Fimalgoritmo