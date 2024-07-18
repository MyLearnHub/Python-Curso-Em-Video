Algoritmo "numero-primo"
Var
   i, number, contDiv: inteiro
Inicio
   i <- 1
   contDiv <- 0
   
   escreva("Digite um número para saber se é primo:")
   leia(number)
   
   repita
      se (number % i = 0) entao
         contDiv <- contDiv + 1
      fimse
      
      i <- i + 1
   ate (i > number)
   
   se (contDiv > 2) entao
      escreva("Esse número não é primo")
   senao
      escreva("Esse número é primo")
   fimse
Fimalgoritmo