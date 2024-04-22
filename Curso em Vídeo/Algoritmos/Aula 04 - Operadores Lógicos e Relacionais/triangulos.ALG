Algoritmo "triangulos"
  Var
    lado1, lado2, lado3 : real
    equilatero, escaleno, triangulo: logico
  Inicio
    escreva("Digite o primeiro lado do seu triângulo: ")
    leia(lado1)
    escreva("Digite o segundo lado do seu triângulo: ")
    leia(lado2)
    escreva("Digite o terceiro lado do seu triângulo: ")
    leia(lado3)
    escreval(" ")
    
    triangulo <- (lado1 < lado2 + lado3) e (lado2 < lado1 + lado3) e (lado3 < lado1 + lado2)
    equilatero <- (lado1 = lado2) e (lado2 = lado3)
    escaleno <- (lado1 <> lado2) e (lado2 <> lado3) e (lado1 <> lado3)
    
    escreval("Pode formar um triângulo?", triangulo)
    escreval("O triângulo é equilátero?", equilatero)
    escreval("O triângulo é escaleno?", escaleno)
Fimalgoritmo