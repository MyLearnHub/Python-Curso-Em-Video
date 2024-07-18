algoritmo "nomeComC"
var
   containsC: vetor[1..10] de caractere
   name: caractere
   i, counterC: inteiro
inicio
   counterC <- 0
   para i <- 1 ate 10 faca
      escreva("Digite um nome: ")
      leia(name)
      
      se (copia(maiusc(name), 1, 1) = "C") entao
         counterC <- counterC + 1
         containsC[counterC] <- name
      fimse
   fimpara
   
   limpatela
   
   escreval("Pessoas com o nome iniciado em 'C':")
   para i <- 1 ate counterC faca
      escreval(containsC[i])
   fimpara
fimalgoritmo