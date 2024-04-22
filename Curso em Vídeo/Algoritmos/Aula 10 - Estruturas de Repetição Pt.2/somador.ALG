Algoritmo "somador"
Var
  value, sum: inteiro
  response: caractere
Inicio
  sum <- 0

  repita
    escreva("Digite um valor:")
    leia(value)
    
    sum <- sum + value
    
    escreva("Quer somar mais um número? [S/N]")
    leia(response)
  ate (response = "N")
  
  escreva("A soma de todos os valores digitados é: ", sum)
Fimalgoritmo