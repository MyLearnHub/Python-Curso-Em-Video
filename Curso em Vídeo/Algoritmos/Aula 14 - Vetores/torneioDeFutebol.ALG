Algoritmo "torneioDeFutebol"
Var
   teamName: vetor[1..3] de caractere
   i, j: inteiro
Inicio
   escreval("---------------------")
   escreval("CAMPEONATO DE FUTEBOL")
   escreval("---------------------")
   para i <- 1 ate 3 faca
      escreva("Nome do ", i, "º time:")
      leia(teamName[i])
   fimpara
   
   limpatela
   
   escreval("--------------------")
   escreval(" TABELA DE PARTIDAS ")
   escreval("--------------------")
   para i <- 1 ate 3 faca
      para j <- 1 ate 3 faca
         se i <> j entao
            escreval(teamName[i], " x ", teamName[j])
         fimse
      fimpara
      escreval()
   fimpara
Fimalgoritmo