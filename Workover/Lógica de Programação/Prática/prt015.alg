algoritmo "Banco"
// Função : Treino de estrutura Caso
// Autor : Paulo Alvares
// Data : 07/01/2023
// Seção de Declarações 
var
   opcao : inteiro
inicio
   escreval("Digite a opção desejada:")
   leia(opcao)
   limpatela
   escolha opcao
   caso 1
      escreval("*********************************")
      escreval("********CONSULTA DE SALDO********")
      escreval("*********************************")
   caso 2
      escreval("*********************************")
      escreval("********EMISSÃO DE EXTRATO*******")
      escreval("*********************************")
   caso 3
      escreval("*********************************")
      escreval("**********FINANCIAMENTOS*********")
      escreval("*********************************")
   caso 4
      escreval("*********************************")
      escreval("*********REALIZAR SAQUES*********")
      escreval("*********************************")
   outrocaso
      escreva("Opção inválida!")
   fimescolha
fimalgoritmo
