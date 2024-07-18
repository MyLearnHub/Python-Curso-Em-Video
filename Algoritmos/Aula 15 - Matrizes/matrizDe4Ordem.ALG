algoritmo "matrizDe4Ordem"
var
   numbers: vetor[1..4, 1..4] de inteiro
   line, column, sumDiagonal, multiplication, max: inteiro
inicio
   sumDiagonal <- 0
   multiplication <- 1
   para line <- 1 ate 4 faca
      para column <- 1 ate 4 faca
         escreva("Digite o número da posição [", line, ",", column, " ]: ")
         leia(numbers[line, column])

         se (line = column) entao
            sumDiagonal <- sumDiagonal + numbers[line, column]
         fimse
      fimpara
   fimpara
   
   para column <- 1 ate 4 faca
      multiplication <- multiplication * numbers[2, column]
   fimpara
   
   para line <- 1 ate 4 faca
      se (numbers[line, 3] > max) entao
         max <- numbers[line, 3]
      fimse
   fimpara

   escreval("   MATRIZ   ")
   escreval("------------")
   para line <- 1 ate 4 faca
      para column <- 1 ate 4 faca
         escreva(numbers[line, column]:4)
      fimpara
      escreval()
   fimpara
   escreval("Soma dos valores da diagonal principal: ", sumDiagonal)
   escreval("Multiplicação dos valores da segunda linha: ", multiplication)
   escreva("Maior valor da 3ª coluna: ", max)
fimalgoritmo