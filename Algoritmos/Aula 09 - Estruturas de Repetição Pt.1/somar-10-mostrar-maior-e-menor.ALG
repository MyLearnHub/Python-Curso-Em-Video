Algoritmo "somar-10-número"
Var
  sum, i, value, maxValue, minValue: inteiro
Inicio
  i <- 1
  enquanto (i <= 3) faca
    escreva("Digite o", i, "º valor a ser somado: ")
    leia(value)

    se (i = 1) entao
      minValue <- value
      maxValue <- value
    fimse

    sum <- sum + value
    i <- i + 1
    
    se (value > maxValue) entao
      maxValue <- value
    fimse
    

    se (value < minValue) entao
      minValue <- value
    fimse
  fimenquanto

  escreval("A soma de todos os valores é:", sum)
  escreval("O maior valor digitado foi:", maxValue)
  escreva("O menor valor digitado foi:", minValue)
Fimalgoritmo