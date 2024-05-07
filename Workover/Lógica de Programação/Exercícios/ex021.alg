algoritmo "Posição na Matriz"
// Função : Treinar Matriz
// Autor : Paulo Alvares
// Data : 11/01/2023
// Seção de Declarações 
var
   matriz : vetor[0..6, 0..6] de caractere

procedimento colocarLetras()
var
   lin, col : inteiro
inicio
   para lin de 0 ate 6 faca
      para col de 0 ate 6 faca
         se lin = col entao
            matriz[lin, col] <- "A"
         senao
            matriz[lin, col] <- "B"
         fimse
      fimpara
   fimpara
fimprocedimento

procedimento mostrarMatriz()
var
   lin, col : inteiro
inicio
   para lin de 0 ate 6 faca
      para col de 0 ate 6 faca
         escreva(matriz[lin, col], " ")
      fimpara
      escreval
   fimpara
fimprocedimento

inicio
   colocarLetras()
   matriz[5,4] <- "C"
   mostrarMatriz()
fimalgoritmo
