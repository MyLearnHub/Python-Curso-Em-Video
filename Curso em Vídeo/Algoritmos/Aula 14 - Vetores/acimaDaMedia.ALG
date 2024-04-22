algoritmo "acimaDaMedia"
var
   name: vetor[1..4] de caractere
   note1, note2, average: vetor[1..4] de real
   i, aboveAverage: inteiro
   sumAverage, averageGroup: real
inicio
   para i <- 1 ate 4 faca
      escreva("Qual o nome do", i, "º aluno? ")
      leia(name[i])
      escreva("Qual a primeira nota de ", name[i], "? ")
      leia(note1[i])
      escreva("Qual a segunda nota de ", name[i], "? ")
      leia(note2[i])

      average[i] <- (note1[i] + note2[i]) / 2
      sumAverage <- sumAverage + average[i]
      limpatela
   fimpara

   escreval("Listagem de Alunos")
   escreval("------------------")
   para i <- 1 ate 4 faca
      escreval("A média de ", name[i]:15, " foi:", average[i])
   fimpara
   
   escreval()
   
   averageGroup <- sumAverage / 4
   
   escreval("A média da sala foi:", averageGroup:4:1)
   para i <- 1 ate 4 faca
      se (average[i] >= averageGroup) entao
         escreval("A nota final de ", name[i], " está acima da média (", average[i], ")")
      fimse
   fimpara
   escreva("Temos", aboveAverage, " alunos acima da média")
fimalgoritmo