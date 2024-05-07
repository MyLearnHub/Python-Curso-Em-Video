algoritmo "Mexendo com Matriz"
// Função : Manipular Matriz
// Autor : Paulo Alvares
// Data : 11/01/2023
// Seção de Declarações 
var
   matriz : vetor[0..9, 0..9] de inteiro

procedimento colocarValores()
var
   lin, col : inteiro
inicio
   para lin de 0 ate 9 faca
      para col de 0 ate 9 faca
         matriz[lin, col] <- randi(50)
      fimpara
   fimpara
fimprocedimento

procedimento somarTudo()
var
   soma, lin, col : inteiro
inicio
   para lin de 0 ate 9 faca
      para col de 0 ate 9 faca
         soma <- soma + matriz[lin, col]
      fimpara
   fimpara
   escreval("A soma dos elementos é:", soma)
fimprocedimento

procedimento contarMenoresDez()
var
   cont, lin, col : inteiro
inicio
   para lin de 0 ate 9 faca
      para col de 0 ate 9 faca
         se matriz[lin, col] < 10 entao
            cont <- cont + 1
         fimse
      fimpara
   fimpara
   escreval("A quantidade dos elementos menor que 10:", cont)
fimprocedimento

inicio
   colocarValores()
   somarTudo()
   contarMenoresDez()
fimalgoritmo
