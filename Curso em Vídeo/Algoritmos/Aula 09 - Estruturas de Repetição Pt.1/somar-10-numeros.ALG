Algoritmo "somar-10-número"
Var
  sum, i, value: inteiro
Inicio
  i <- 1
  enquanto (i <= 3) faca
    escreva("Digite o", i, "º valor a ser somado: ")
    leia(value)
    
    sum <- sum + value
    i <- i + 1
  fimenquanto
  
  escreva("A soma de todos os valores é:", sum)
Fimalgoritmo