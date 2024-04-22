algoritmo "analisadorDeNomes"
var
   name: caractere
   i: inteiro
inicio
   escreva("Vamos análisar o seu nome! Digite ele aqui: ")
   leia(name)

   escreval("Seu nome possui:", compr(name), " letras")
   escreval("Sua nome em letras maiúsculas é: ", maiusc(name))
   escreval("Sua nome em letras minúsculas é: ", minusc(name))
   escreval("A primeira letra do seu nome é: ", copia(maiusc(name), 1, 1))
   escreval("A última letra do seu nome é: ", copia(maiusc(name), compr(name), 1))
   se(pos("A", maiusc(name)) = verdadeiro) entao
      escreval("Seu nome possui a letra 'A' na posição:", pos("A", maiusc(name)))
      escreval("O código da letra 'A' é:", asc("A"))
      escreval("O caractere correspondente ao código 65 é: ", carac(65))
   fimse
   escreva("Seu nome ao contrário é: ")
   para i <- compr(name) ate 1 passo -1 faca
      escreva(copia(maiusc(name), i, 1))
   fimpara
fimalgoritmo