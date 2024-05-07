algoritmo "Quiz"
// Função : Quiz
// Autor : Paulo Alvares
// Data : 06/01/2023
// Seção de Declarações 
var
   cont_exatas, cont_humanas, resultado : inteiro
inicio
   escreval("================================================")
   escreval("       QUIZ - CIÊNCIAS HUMANAS OU EXATAS?       ")
   escreval("================================================")
   escreval("Digite 1 para Sim e 2 para Não seguido de Enter.")
   escreval("------------------------------------------------")
   escreval("")
   
   escreva("Você gosta de matemática?")
   leia(resultado)
   se resultado = 1 entao
      cont_exatas <- cont_exatas + 1
   fimse
   
   escreva("Você gosta de ler?")
   leia(resultado)
   se resultado = 1 entao
      cont_humanas <- cont_humanas + 1
   fimse
   
   escreva("Você se sente atraído por questões de raciocínio lógico?")
   leia(resultado)
   se resultado = 1 entao
      cont_exatas <- cont_exatas + 1
   fimse
   
   escreva("Você se sente atraído a questões sociais?")
   leia(resultado)
   se resultado = 1 entao
      cont_humanas <- cont_humanas + 1
   fimse
   
   escreval("")
   escreval("================================================")
   escreval("               RESULTADOS DO QUIZ               ")
   escreval("================================================")
   escreval("")
   se cont_humanas > cont_exatas entao
      escreval("Você tem tendência ás CIÊNCIAS HUMANAS")
   senao
      se cont_exatas > cont_humanas entao
         escreval("Você tem tendência ás CIÊNCIAS EXATAS")
      senao
         escreval("Houve um empate na sua pontuação. Não foi possível avaliar suas tendências de estudo")
      fimse
   fimse
   
   escreval("Pontuação de Humanas:", cont_humanas)
   escreval("Pontuação de Exatas:", cont_exatas)
fimalgoritmo
