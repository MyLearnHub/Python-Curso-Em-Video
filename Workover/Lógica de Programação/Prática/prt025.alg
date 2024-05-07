algoritmo "Fatorial"
// Função : Cálculo de fatorial
// Autor : Paulo Alvares
// Data : 11/01/2023
// Seção de Declarações 
var

funcao calcularFatorial(numero : inteiro) : inteiro
var
   fat, i : inteiro
inicio
   fat <- 1
   para i de numero ate 2 passo -1 faca
      fat <- fat * i
   fimpara
   retorne(fat)
fimfuncao

inicio
   escreva(calcularFatorial(5))
fimalgoritmo
