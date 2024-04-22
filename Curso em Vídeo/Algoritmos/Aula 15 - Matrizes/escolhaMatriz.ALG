algoritmo "escolhaMatriz"
var
   numbers: vetor[1..4, 1..4] de inteiro
   line, column, choice: inteiro
inicio
   para line <- 1 ate 4 faca
      para column <- 1 ate 4 faca
         escreva("Digite o número da posição [", line, ", ", column, " ]: ")
         leia(numbers[line, column])
      fimpara
   fimpara

   limpatela

   repita
      escreval("========================")
      escreval("     MENU DE OPÇÕES     ")
      escreval("========================")
      escreval("[1] Mostrar matriz completa")
      escreval("[2] Mostrar diagonal principal")
      escreval("[3] Mostrar triângulo superior")
      escreval("[4] Mostrar triângulo inferior")
      escreval("[5] Sair")
      escreva("======== OPÇÃO: ")
      leia(choice)

      escolha choice
      caso 1
         para line <- 1 ate 4 faca
            para column <- 1 ate 4 faca
               escreva(numbers[line, column]:4)
            fimpara
            escreval()
         fimpara
      caso 2
         para line <- 1 ate 4 faca
            escreval(numbers[line, line]:4)
            para column <- 1 ate 4 faca
               escreva("    ")
            fimpara
            escreval()
         fimpara
      caso 3
         para line <- 1 ate 3 faca
            escreva("    ")
            para column <- line + 1 ate 4 faca
               escreva(numbers[line, column]:4)
            fimpara
            escreval()
            para column <- 1 ate line faca
               escreva("    ")
            fimpara
         fimpara
         escreval()
      caso 4
         para line <- 2 ate 4 faca
            escreval()
            para column <- 1 ate line - 1 faca
               escreva(numbers[line, column]:4)
            fimpara
         fimpara
         escreval()
      fimescolha
   ate(choice = 5)
   escreva("Saindo... Até mais!")
fimalgoritmo