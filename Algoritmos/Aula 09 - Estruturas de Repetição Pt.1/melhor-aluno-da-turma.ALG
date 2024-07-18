Algoritmo "melhor-aluno-da-turma"
Var
  qtStudents, i: inteiro
  name, bestStudent: caractere
  note, bestNote: real
Inicio
  i <- 1

  escreval("------------------------")
  escreval(" Escola Santa Paciência ")
  escreval("------------------------")
  escreval("Quantos alunos a turma tem?")
  leia(qtStudents)
  escreval("------------------------")
  
  enquanto (i <= qtStudents) faca
    escreval(i, "º ALUNO")
    escreval("Nome do Aluno: ")
    leia(name)
    escreval("Nota de ", name, ": ")
    leia(note)
    escreval("------------------------")
    
    se (note >= bestNote) entao
      bestStudent <- name
      bestNote <- note
    fimSe
    
    i <- i + 1
  fimEnquanto
  
  escreva("O melhor aproveitamento foi de ", bestStudent, " com a nota: ", bestNote)
  
Fimalgoritmo