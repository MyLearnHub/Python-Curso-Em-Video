Algoritmo "esta-apto-a-dirigir"
  Var
    currentYear, birthYear, age: inteiro
    permission: caractere
  Inicio
    escreval("--------------------------")
    escreval(" DEPARTAMENTO DE TRÂNSITO ")
    escreval("--------------------------")
    escreva("Em que ano estamos? ")
    leia(currentYear)
    escreva("Qual o ano do seu nascimento? ")
    leia(birthYear)
    
    age <- currentYear - birthYear
    
    se (age >= 18) entao
      permission <- " APTO A TIRAR CARTEIRA"
    senao
      permission <- " INAPTO A TIRAR CARTEIRA"
    fimse
    
    escreval(" ")
    escreval("-------- STATUS --------")
    escreval(" IDADE:", age, " ANOS")
    escreval(permission)
    escreval("------------------------")
Fimalgoritmo