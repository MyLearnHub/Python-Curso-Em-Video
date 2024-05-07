algoritmo "Soma e Média"
// Função : Testar estruturas de repetição
// Autor : Paulo Alvares
// Data : 10/01/2023
// Seção de Declarações
var
   valor, soma, cont : inteiro
   media : real
inicio
   enquanto cont < 10 faca
      escreval("Digite um número:")
      leia(valor)
      soma <- soma + valor
      cont <- cont + 1
   fimenquanto
   media <- soma / 10
   escreval("A soma total dos valores é:", soma)
   escreva("Já a média é:", media)
fimalgoritmo
