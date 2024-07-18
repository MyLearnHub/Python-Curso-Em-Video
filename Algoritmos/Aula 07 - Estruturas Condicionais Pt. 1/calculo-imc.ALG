Algoritmo "calculo-imc"
  Var
    mass, height, imc: real
  Inicio
    escreva("Me diga sua massa (Kg):")
    leia(mass)
    escreva("Me diga também sua altura (M):")
    leia(height)
    
    imc <- mass / (height ^ 2)
    
    escreval ("Seu IMC é:", imc:5:2)
    
    se (imc >= 18.5) e (imc < 25) entao
      escreva("Parabéns! Você está no seu peso ideal")
    senao
      escreva("Seu peso não está ideal, procure um nutricionista")
    fimse
Fimalgoritmo