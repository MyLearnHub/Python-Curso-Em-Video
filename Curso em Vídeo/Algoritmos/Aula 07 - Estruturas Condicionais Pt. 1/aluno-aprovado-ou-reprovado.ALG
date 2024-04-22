Algoritmo "aluno-aprovado-ou-reprovado"
  Var
    note1, note2, average: real
    approved: caractere
  Inicio
    escreval("-----------------------")
    escreval(" ESCOLA JAVALI CANSADO ")
    escreval("-----------------------")
    escreva("Primeira Nota: ")
    leia(note1)
    escreva("Segunda Nota: ")
    leia(note2)
    
    average <- (note1 + note2) / 2
    
    se average >= 7 entao
      approved <- "APROVADO"
    senao
      approved <- "REPROVADO"
    fimse
    
    escreval("-----------------------")
    escreval(" MÉDIA:", average)
    escreval(" ALUNO ", approved)
    escreval("-----------------------")
Fimalgoritmo