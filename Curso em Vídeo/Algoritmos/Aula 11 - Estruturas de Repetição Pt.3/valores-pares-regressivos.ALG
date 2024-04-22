Algoritmo "valores-pares-regressivos"
Var
   i, number: inteiro
Inicio
   escreva("Digite um número para ver os pares: ")
   leia(number)
   
   se (number % 2 = 1) entao
      number <- number - 1
   fimse

   para i <- number ate 0 passo -2 faca
      escreval(i)
   fimpara
Fimalgoritmo