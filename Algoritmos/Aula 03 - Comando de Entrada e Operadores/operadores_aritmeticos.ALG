Algoritmo "operadores_aritmeticos"
  Var
    absNumber, integer : inteiro
    exponentiation, squareRoot, radianDegree : real
  Inicio
    absNumber <- abs(-50)
    escreval("Valor absoluto de -50 é:", absNumber)
    escreval("-----------------------------------")
    
    exponentiation <- exp(9, 5)
    escreval("O número 9 elevado a 5 é:", exponentiation)
    escreval("-----------------------------------")
    
    squareRoot <- raizq(81)
    escreval("A raiz quadrada de 81 é:", squareRoot)
    escreval("-----------------------------------")
    
    integer <- int(raizq(90))
    escreval("A parte inteira, da raiz quadrada de 90 é:", integer)
    escreval("-----------------------------------")
    
    radianDegree <- sen(grauprad(90))
    escreva("O seno de 90 graus radianos é:", radianDegree)
Fimalgoritmo