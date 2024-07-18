Algoritmo "escolha-caso"
Var
   choice: inteiro
   value: real
Inicio
   escreval("---------------------------")
   escreval("     CRIANÇA ESPERANÇA     ")
   escreval("---------------------------")
   escreval(" Muito obrigado por ajudar ")
   escreval(" [1] para doar R$10 ")
   escreval(" [2] para doar R$25 ")
   escreval(" [3] para doar R$50 ")
   escreval(" [4] para doar outros valores ")
   escreval(" [5] para cancelar ")
   leia(choice)
   
   escolha choice
     caso 1
        value <- 10
     caso 2
        value <- 25
     caso 3
        value <- 50
     caso 4
        escreva("Quanto deseja doar? R$")
        leia(value)
     caso 5
        value <- 0
   fimescolha
   
   escreval("---------------------------")
   escreval(" SUA DOAÇÃO FOI DE: R$", value)
   escreval(" MUITO OBRIGADO! ")
   escreval("---------------------------")
Fimalgoritmo