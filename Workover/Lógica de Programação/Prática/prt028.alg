algoritmo "Matriz"
// Função : Aprender Matriz
// Autor : Paulo Alvares
// Data : 11/01/2023
// Seção de Declarações 
var
   velha : vetor[0..2, 0..2] de caractere
   lin, col : inteiro
inicio
   para lin de 0 ate 2 faca
      para col de 0 ate 2 faca
         velha[lin, col] <- "X"
      fimpara
   fimpara
   
   para lin de 0 ate 2 faca
      para col de 0 ate 2 faca
         escreva(velha[lin, col], " ")
      fimpara
      escreval
   fimpara
fimalgoritmo
