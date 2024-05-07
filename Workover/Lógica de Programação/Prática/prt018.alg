algoritmo "Maior que 7?"
// Função : Testar variáveis
// Autor : Paulo Alvares
// Data : 10/01/2023
// Seção de Declarações 
var
   valor, quantidade, cont : inteiro
inicio
   enquanto cont < 7 faca
      escreval("Digite um número:")
      leia(valor)
      se valor > 50 entao
         quantidade <- quantidade + 1
      fimse
      cont <- cont + 1
   fimenquanto
   escreval("Dos valores digitados,", quantidade, " são maiores que 50")
fimalgoritmo
