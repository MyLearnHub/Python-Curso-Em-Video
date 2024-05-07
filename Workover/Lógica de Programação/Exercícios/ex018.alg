algoritmo "Soma e Mostra"
// Função : Treinar Vetores
// Autor : Paulo Alvares
// Data : 11/01/2023
// Seção de Declarações 
var
   numero : vetor[0..4] de inteiro
   i, soma : inteiro
inicio
   para i de 0 ate 4 faca
      escreva("Digite um número:")
      leia(numero[i])
      soma <- soma + numero[i]
   fimpara
   escreval("")
   escreval(soma, ", é a soma entre:")
   para i de 0 ate 4 faca
      escreval(numero[i])
   fimpara
fimalgoritmo
