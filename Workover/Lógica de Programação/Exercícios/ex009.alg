algoritmo "Veículo"
// Função : Somador
// Autor : Paulo Alvares
// Data : 07/01/2023
// Seção de Declarações 
var
   preco, somador, precofinal : real
   resposta, contador : inteiro
inicio
   escreva("Digite o preço inicial do veículo desejado:")
   leia(preco)
   
   escreva("Gostaria de incluir algum acessório?(1 para Sim e 2 para Não)")
   leia(resposta)
   se resposta = 1 entao
      escreval("Gostaria de adicionar Ar-condicionado?")
      leia (resposta)
      se resposta = 1 entao
         somador <- somador + 3000
         contador <- contador + 1
      fimse
      
      escreval("Gostaria de adicionar Direção Hidráulica?")
      leia(resposta)
      se resposta = 1 entao
         somador <- somador + 1500
         contador <- contador + 1
      fimse
      
      escreval("Gostaria de adicionar Alarme?")
      leia(resposta)
      se resposta = 1 entao
         somador <- somador + 500
         contador <- contador + 1
      fimse
      
      escreval("Gostaria de adicionar Alto-Falantes?")
      leia(resposta)
      se resposta = 1 entao
         somador <- somador + 1000
         contador <- contador + 1
      fimse
   fimse
   precofinal <- preco + somador
   escreval("Preço inicial:", preco)
   escreval("Quantidade de acessórios incluídos:", contador)
   escreval("Valor total dos acessórios:", somador)
   escreval("Preço final:", precofinal)
fimalgoritmo
