Algoritmo "quantos-valores-entre-0-e-10"
Var
   i, contVal, number: inteiro
Inicio
   para i <- 1 ate 6 passo 1 faca
      escreva("Digite um número: ")
      leia(number)
      
      se (number >= 0) e (number <= 10) entao
         contVal <- contVal + 1
      fimse
   fimpara
   escreva(contVal, " números estão entre 0 e 10")
Fimalgoritmo