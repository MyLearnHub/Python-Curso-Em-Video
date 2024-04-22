Algoritmo "imposto"
  Var
    productValue, payValue: real
  Inicio
    escreva("Qual o valor do produto?")
    leia(productValue)
    
    payValue <- productValue * 60 / 100
    
    escreva("O valor a ser pago é: R$", payValue:5:2)
Fimalgoritmo