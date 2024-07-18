algoritmo "ordenacaoDeVetor"
var
   numbers: vetor[1..10] de inteiro
   i, j, temporary: inteiro
inicio
   para i <- 1 ate 10 faca
      escreva("Digite um número: ")
      leia(numbers[i])
   fimpara
   
   para i <- 1 ate 9 faca
      para j <- i + 1 ate 10 faca
         se (numbers[i] > numbers[j]) entao
            temporary <- numbers[i]
            numbers[i] <- numbers[j]
            numbers[j] <- temporary
         fimse
      fimpara
   fimpara
   
   para i <- 1 ate 10 faca
      escreva(numbers[i])
   fimpara
fimalgoritmo