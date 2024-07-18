algoritmo "funcoes-de-string"
var
   phrase: caractere
inicio
   escreva("Digite uma frase simples (Ex: Eu adoro codar): ")
   leia(phrase)
   
   escreval("O tamanho da sua frase é de:", compr(phrase), " caracteres")
   escreval("Pulando 3 caracteres e exibindo só 5 temos: ", copia(phrase, 4, 5))
   escreval("Sua frase em letras maiúsculas é: ", maiusc(phrase))
   escreval("Sua frase em letras minúsculas é: ", minusc(phrase))
   escreval("Buscando a posição de início da palavra 'Eu':", pos("Eu", phrase))
   escreval("O código da sua frase é:", asc(phrase))
   escreva("O caractere correspondente ao código 80 é: ", carac(80))
fimalgoritmo