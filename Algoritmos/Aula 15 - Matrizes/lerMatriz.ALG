algoritmo "lerMatriz"
var
   numbers: vetor[1..3, 1..2] de inteiro
   line, column: inteiro
inicio
   para line <- 1 ate 3 faca
      para column <- 1 ate 2 faca
         escreva("Digite um número da posição [", line, ",", column," ]: ")
         leia(numbers[line, column])
      fimpara
   fimpara

   para line <- 1 ate 3 faca
      para column <- 1 ate 2 faca
         escreva(numbers[line, column]:3)
      fimpara
      escreval()
   fimpara
fimalgoritmo