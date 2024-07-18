algoritmo "vetor"
var
   numbers: vetor[1..6] de inteiro
   i: inteiro
inicio
   para i <- 1 ate 6 faca
      escreva("Digite o", i, "º número: ")
      leia(numbers[i])
   fimpara
   
   escreva("Seu vetor ficou assim: [")
   para i <- 1 ate 6 faca
      se (i = 6) entao
         escreva(numbers[i])
      senao
         escreva(numbers[i], ",")
      fimse
   fimpara
   escreva("]")
fimalgoritmo