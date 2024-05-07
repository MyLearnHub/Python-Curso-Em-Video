algoritmo "Multiplicando Vetores"
// Função : Multiplicar dados de um vetor
// Autor : Paulo Alvares
// Data : 11/01/2023
// Seção de Declarações 
var
   numero, multiplicado : vetor[0..9] de inteiro
   i : inteiro
inicio
   para i de 0 ate 9 faca
      escreva("Digite um número:")
      leia(numero[i])
      multiplicado[i] <- numero[i] * 5
   fimpara
   escreval("")
   para i de 0 ate 9 faca
      escreval(numero[i]," - ", multiplicado[i])
   fimpara
fimalgoritmo
