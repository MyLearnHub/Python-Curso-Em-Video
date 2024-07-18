algoritmo "matrizPar"
var
   numbers: vetor[1..3, 1..3] de inteiro
   line, column, totalEven: inteiro
inicio
   para line <- 1 ate 3 faca
      para column <- 1 ate 3 faca
         escreva("Digite o número da posição [", line, ", ", column, " ]: ")
         leia(numbers[line, column])
      fimpara
   fimpara

   escreval("MATRIZ:")
   escreval("-------")
   totalEven <- 0
   para line <- 1 ate 3 faca
      para column <- 1 ate 3 faca
         se (numbers[line, column] % 2 = 0) entao
            escreva("{", numbers[line, column]:2, " }")
            totalEven <- totalEven + 1
         senao
            escreva(numbers[line, column]:4)
         fimse
      fimpara
      escreval()
   fimpara
   escreva("Números pares: ", totalEven)
fimalgoritmo