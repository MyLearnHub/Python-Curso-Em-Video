algoritmo "Positivo, negativo ou zero"
// Função : Testar valor númerico
// Autor : Paulo Alvares
// Data : 07/01/2023
// Seção de Declarações 
var
   numero : inteiro
inicio
   escreval("Digite um valor:")
   leia(numero)
   se numero > 0 entao
      escreva("Número Positivo")
   senao
      se numero = 0 entao
         escreva("Zero")
      senao
         escreva("Número Negativo")
      fimse
   fimse
fimalgoritmo
