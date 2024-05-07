algoritmo "Categorias"
// Função : Avaliar atletas
// Autor : Paulo Alvares
// Data : 07/01/2023
// Seção de Declarações 
var
   idade : inteiro
inicio
   escreval("Digite sua idade:")
   leia(idade)
   se idade < 18 entao
      escreva("Júnior")
   senao
      se (idade >= 18) e (idade < 35) entao
         escreva("Adulto")
      senao
         escreva("Sênior")
      fimse
   fimse
fimalgoritmo
