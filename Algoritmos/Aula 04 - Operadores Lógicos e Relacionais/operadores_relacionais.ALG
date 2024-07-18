Algoritmo "operadores_relacionais"
  Var
  value01, value02, value03 : inteiro
  Inicio
  value01 <- 2
  value02 <- 3
  value03 <- 5
  
  escreval("value01 é maior que value02?", value01 > value02)
  escreval("value01 é igual a value02?", value01 = value02)
  escreval("value01 é diferente de value02?", value01 <> value02)
  escreval("value01 é maior que 2?", value01 > 2)
  escreval("value01 é maior ou igual a 2?", value01 >= 2)
  escreval("value03 é a soma de value01 e value02?", value03 = value01 + value02)
  escreval("value03 é maior ou igual a value02 elevado a value01?", value03 = value02 ^ value01)
  escreval("value03 é menor ou igual a value02 elevado a value01?", value03 <= value02 ^ value01)
  escreval("value02 é menor ou igual ao resto de divisão por 2 de value03?", value02 <= value02 % 2)
  escreval("1 é igual ao resto de divisão por 2 de value03?", 1 = value02 % 2)
Fimalgoritmo