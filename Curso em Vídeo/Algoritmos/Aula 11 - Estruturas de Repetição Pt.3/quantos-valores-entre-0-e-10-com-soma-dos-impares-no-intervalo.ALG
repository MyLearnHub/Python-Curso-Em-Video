Algoritmo "quantos-valores-entre-0-e-10-com-soma-dos-impares-no-intervalo"
Var
   i, contVal, number, sum: inteiro
Inicio
   para i <- 1 ate 6 passo 1 faca
      escreva("Digite um número: ")
      leia(number)

      se (number >= 0) e (number <= 10) entao
         contVal <- contVal + 1
         se (number % 2 = 1) entao
            sum <- sum + number
         fimse
      fimse
   fimpara
   escreval(contVal, " números estão entre 0 e 10")
   escreva("A soma dos valores impares é: ", sum)
Fimalgoritmo