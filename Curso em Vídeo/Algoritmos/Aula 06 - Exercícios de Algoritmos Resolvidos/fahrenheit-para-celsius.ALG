Algoritmo "fahrenheit-para-celsius"
  Var
    fahrenheit, celsius: real
  Inicio
    escreva("Qual a temperatura em Fº?")
    leia(fahrenheit)
    
    celsius <- (fahrenheit - 32) / 1.8
    
    escreva("Atualmente faz ", celsius:4:1, "Cº!")
Fimalgoritmo