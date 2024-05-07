algoritmo "Análisando Pessoas"
// Função : Análisar dados e valores de pessoas
// Autor : Paulo Alvares
// Data : 07/01/2023
// Seção de Declarações 
var
   idade, totalidade, irmaos, totalirmaos : inteiro
   mediaidade : real
inicio
   escreval("Olá Marcos, digite sua idade:")
   leia(idade)
   totalidade <- totalidade + idade
   escreval("Ótimo, agora digite a quantidade de irmâos que você tem:")
   leia(irmaos)
   totalirmaos <- totalirmaos + irmaos
   
   escreval("Olá Joice, digite sua idade:")
   leia(idade)
   totalidade <- totalidade + idade
   escreval("Ótimo, agora digite a quantidade de irmâos que você tem:")
   leia(irmaos)
   totalirmaos <- totalirmaos + irmaos
   
   escreval("Olá Luis, digite sua idade:")
   leia(idade)
   totalidade <- totalidade + idade
   escreval("Ótimo, agora digite a quantidade de irmâos que você tem:")
   leia(irmaos)
   totalirmaos <- totalirmaos + irmaos
   
   mediaidade <- totalidade / 3
   
   escreval("A soma das idades:", totalidade)
   escreval("A média das idades:", mediaidade)
   escreval("O total de irmãos:", totalirmaos)
fimalgoritmo
