Algoritmo "repetir-fatorial"
Var
   i, value, factorial: inteiro
   response: caractere
Inicio
   repita
      escreva("Qual número gostaria de saber o valor fatorial?")
      leia(value)

      i <- value
      factorial <- 1

      repita
         factorial <- factorial * i
         i <- i - 1
      ate (i < 1)

      escreval("Fatorial de", value, ":", factorial)
      escreva("Gostaria de repetir? [S/N]")
      leia(response)
      limpatela
   ate (response = "N")
Fimalgoritmo