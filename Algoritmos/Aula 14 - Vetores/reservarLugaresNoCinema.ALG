algoritmo "reservarLugarNoCinema"
var
   reserved: vetor [1..19] de caractere
   i, option: inteiro
   reservation: caractere
inicio
   repita
      limpatela
      para i <- 1 ate 10 faca
         se (reserved[i] = "") entao
            escreva ("[ B", i:2, " ]")
         senao
            escreva ("[ --- ]")
         fimse
      fimpara
      escreval()
      escreval("------------------------------------------------------------------------")
      escreva("Reservar a cadeira: B")
      leia(option)
      se (reserved[option] = "") entao
         reserved[option] <- "X"
         escreval("Cadeira B", option, " RESERVADA!")
      senao
         escreval("ERRO: Lugar Ocupado!")
      fimse
      escreva("Quer reservar outro? [S/N] ")
      leia(reservation)
   ate (reservation = "N")
fimalgoritmo