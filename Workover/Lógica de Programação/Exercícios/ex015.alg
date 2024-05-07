algoritmo "Exercício Repetido"
// Função : Média e Soma
// Autor : Paulo Alvares
// Data : 10/01/2023
// Seção de Declarações 
var
   cont, soma, valor : inteiro
   media : real
inicio
   para cont de 1 ate 5 faca
      escreval("Digite um número:")
      leia(valor)
      soma <- soma + valor
   fimpara
   media <- soma / 5
   escreval("A soma entre os valores é:", soma)
   escreva("A média entre os valores é:", media)
fimalgoritmo
