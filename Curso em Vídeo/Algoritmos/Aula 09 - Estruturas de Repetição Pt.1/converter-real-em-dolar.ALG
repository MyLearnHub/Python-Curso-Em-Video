Algoritmo "converter-real-em-dolar"
Var
   i, qtConversao: inteiro
   reais, dolares: real
Inicio
   i <- 1

   escreva("Quantas conversões de valores deseja realizar?")
   leia(qtConversao)

   enquanto (i <= qtConversao) faca
     escreva("Quantos R$ você tem?")
     leia(reais)

     dolares <- reais / 5.06
     
     escreval("Com R$", reais, " ,você pode comprar: US$", dolares:5:2, " doláres!")
     
     i <- i + 1
   fimEnquanto
Fimalgoritmo