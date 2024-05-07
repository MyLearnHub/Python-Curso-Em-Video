algoritmo "M.M.C"
// Função : Fazer M.M.C de um número
// Autor : Paulo Alvares
// Data : 10/01/2023
// Seção de Declarações 
var
   valor1, valor2, resultado1, resultado2, cont1, cont2, sair: inteiro
inicio
   escreval("Digite o primeiro número:")
   leia(valor1)
   escreval("Digite o segundo número:")
   leia(valor2)
   para cont1 de 1 ate valor1 * valor2 faca
      resultado1 <- valor1 * cont1
      para cont2 de 1 ate valor1 * valor2 faca
         resultado2 <- valor2 * cont2
         se resultado1 = resultado2 entao
            escreva("O M.M.C entre", valor1, " e", valor2, " é:", resultado1)
            sair <- 1
            interrompa
         fimse
      fimpara
      se sair = 1 entao
         interrompa
      fimse
   fimpara

fimalgoritmo
