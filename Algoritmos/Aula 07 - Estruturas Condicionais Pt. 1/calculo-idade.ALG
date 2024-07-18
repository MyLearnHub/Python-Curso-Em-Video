Algoritmo "calculo-idade"
  Var
    currentYear, birthYear, age: inteiro
  Inicio
    escreva("Olá, em que ano nós estamos?")
    leia(currentYear)
    escreva("Ótimo, e em qual ano você nasceu?")
    leia(birthYear)

    age <- currentYear - birthYear

    escreval("Uau, então você já tem", age, " anos!!!")
    
    se age > 21 entao
      escreva("Você já está na maioridade, legal!!!")
    fimse
Fimalgoritmo