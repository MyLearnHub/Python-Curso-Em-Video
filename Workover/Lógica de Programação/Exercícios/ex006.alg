algoritmo "Porcentagem"
// Função : Cálculo de Porcentagem
// Autor : Paulo Alvares
// Data : 05/01/2023
// Seção de Declarações 
var
   valor1, valor2, acrescimo, desconto : real
inicio
   escreval("Digite o valor a ser acrescentado:")
   leia(valor1)
   acrescimo <- valor1 + valor1 * 30 / 100
   escreval("Digite o valor a ser descontado:")
   leia(valor2)
   desconto <- valor2 - valor2 * 25 / 100
   escreval("O resultado de", valor1, " com acrescimo de 30% fica:", acrescimo)
   escreval("O resultado de", valor2, " com desconto de 25% fica:", desconto)
   
fimalgoritmo
