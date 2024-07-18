Algoritmo "escolhendo-pessoas"
Var
   gender, response: caractere
   age, hairColor, manEspec, womanEspec: inteiro
Inicio
   repita
      escreval("==========================")
      escreval("    SELETOR DE PESSOAS    ")
      escreval("==========================")
      escreva("Qual o sexo? [M/F]")
      leia(gender)
      escreva("Qual a idade?")
      leia(age)
      escreval("Qual a cor do cabelo?")
      escreval("---------------------")
      escreval("[1] Preto")
      escreval("[2] Castanho")
      escreval("[3] Loiro")
      escreval("[4] Ruivo")
      leia(hairColor)
      
      se (gender = "M") entao
         se (age > 18) entao
            se (hairColor = 2) entao
               manEspec <- manEspec + 1
            fimse
         fimse
      senao
         se (age >= 25) e (age <= 30) entao
            se (hairColor = 3) entao
               womanEspec <- womanEspec + 1
            fimse
         fimse
      fimse
      
      escreva("Quer continuar? [S/N]")
      leia(response)
   ate (response = "N")
   escreval("Homens com mais de 18 anos e de cabelo castanho: ", manEspec)
   escreval("Mulheres entre 25 e 30 anos e de cabelo loiro: ", womanEspec)
Fimalgoritmo