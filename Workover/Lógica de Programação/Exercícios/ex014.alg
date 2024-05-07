algoritmo "Múltiplos de 3"
// Função : Mostrar os valores múltiplos de 3
// Autor : Paulo Alvares
// Data : 10/01/2023
// Seção de Declarações
var
   cont : inteiro
inicio
   cont <- 20
   repita
      se cont % 3 = 0 entao
         escreval(cont)
      fimse
      cont <- cont + 1
   ate cont > 50
fimalgoritmo
