algoritmo "Número Triângular"
// Função : Verificar se um número é triângular
// Autor : Paulo Alvares
// Data : 10/01/2023
// Seção de Declarações 
var
   valor, cont, controle: inteiro
   teste : logico
inicio
   escreval("Digite um número:")
   leia(valor)
   para cont de 0 ate valor faca
      controle <- cont * (cont + 1) * (cont + 2)
      se controle = valor entao
         teste <- verdadeiro
         interrompa
      fimse
   fimpara
   se teste = verdadeiro entao
      escreva("Esse número é triângular")
   senao
      escreva("Esse número não é triângular")
   fimse
fimalgoritmo
