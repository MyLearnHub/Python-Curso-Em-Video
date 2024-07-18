Algoritmo "detector-pesado"
Var
   i: inteiro
   name, heavyName: caractere
   weight, heavyWeight: real

Procedimento header()
Inicio
   limpatela
   escreval("------------------------------------")
   escreval(" D E T E C T O R   DE   P E S A D O ")
   escreval("Maior peso até agora: ", heavyWeight, "Kg")
   escreval("------------------------------------")
FimProcedimento

Inicio
   header()
   para i <- 1 ate 5 faca
      escreva("Digite o nome: ")
      leia(name)
      escreva("Digite o peso de ", name, ": ")
      leia(weight)

      se (weight > heavyWeight) entao
         heavyWeight <- weight
         heavyName <- name
      fimse

      header()
   fimpara
   header()
   escreval("A pessoa mais pesada é ", heavyName, ", com ", heavyWeight, "Kg")
Fimalgoritmo