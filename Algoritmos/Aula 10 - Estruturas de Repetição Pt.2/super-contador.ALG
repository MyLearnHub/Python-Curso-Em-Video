Algoritmo "super-contador"
Var
   response, i: inteiro
Inicio
   repita
      escreval("=================")
      escreval("|    M E N U    |")
      escreval("=================")
      escreval("| [1] De 1 a 10 |")
      escreval("| [2] De 10 a 1 |")
      escreval("| [3] Sair      |")
      escreval("=================")
      leia(response)

      se (response = 1) entao
         i <- 1
         repita
            escreva(i, "...")
            i <- i + 1
         ate (i > 10)
      senao
         se (response = 2) entao
            i <- 10
            repita
               escreva(i, "...")
               i <- i - 1
            ate (i < 1)
         fimse
      fimse
      escreval(" ")
   ate (response = 3)
   escreva("SAINDO...")
Fimalgoritmo