Algoritmo "corrigindoProvas"
Var
   template, response, name: vetor[1..5] de caractere
   finalAverage: vetor[1..5] de real
   i, j: inteiro
   sumAverage, averageGroup: real
Inicio
   escreval("------------------------------")
   escreval("PASSO 1 - Cadastro de Gabarito")
   escreval("------------------------------")
   para i <- 1 ate 5 faca
      escreva("Questão", i, ": ")
      leia(template[i])
   fimpara

   limpatela

   para i <- 1 ate 3 faca
      escreval("------------")
      escreval(i, "º ALUNO")
      escreval("------------")
      escreva("Nome: ")
      leia(name[i])
      escreval("Respostas de ", name[i])
      finalAverage[i] <- 0
      para j <- 1 ate 5 faca
         escreva("Questão", j,": ")
         leia(response[j])

         se (response[j] = template[j]) entao
            finalAverage[i] <- finalAverage[i] + 2
         fimse
      fimpara
      limpatela
   fimpara

   limpatela

   sumAverage <- 0
   para i <- 1 ate 3 faca
      sumAverage <- sumAverage + finalAverage[i]
   fimpara
   averageGroup <- sumAverage / 3

   escreval("------------------")
   escreval("   NOTAS FINAIS   ")
   escreval("------------------")
   para i <- 1 ate 3 faca
      escreval(name[i], " - ", finalAverage[i]:4:1)
   fimpara
   escreval("------------------")
   escreva("Média da Turma:", averageGroup:4:1)
Fimalgoritmo