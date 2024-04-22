Algoritmo "aniversario"
  Var
    currentYear, birthYear, age: inteiro
  Inicio
    escreva("Olá, em que ano nós estamos?")
    leia(currentYear)
    escreva("Ótimo, e em qual ano você nasceu?")
    leia(birthYear)
    
    age <- currentYear - birthYear
    
    escreva("Uau, então você já tem", age, " anos!!!")
Fimalgoritmo