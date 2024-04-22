algoritmo "matrizIdentidade"
var
   matrix: vetor[1..3, 1..3] de inteiro
   line, column: inteiro
inicio
   para line <- 1 ate 3 faca
      para column <- 1 ate 3 faca
         se (line = column) entao
            matrix[line, column] <- 1
         senao
            matrix[line, column] <- 0
         fimse
      fimpara
   fimpara

   para line <- 1 ate 3 faca
      para column <- 1 ate 3 faca
         escreva(matrix[line, column]:4)
      fimpara
      escreval()
   fimpara
fimalgoritmo