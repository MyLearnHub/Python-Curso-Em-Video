algoritmo "Vendas"
// Função : Cálculo de Porcentagem
// Autor : Paulo Alvares
// Data : 05/01/2023
// Seção de Declarações 
var
   salario, vendas, comissao, salfinal : real
inicio
   escreva("Digite seu salário:")
   leia(salario)
   escreva("Digite o total de vendas no mês:")
   leia(vendas)
   comissao <- vendas * 15 / 100
   salfinal <- salario + comissao
   escreval("Seu salário atual é:", salario)
   escreval("Você realizou:", vendas ," esse mês")
   escreval("E o valor da comissão desse mês é:", comissao)
   escreva("Portanto, seu salário final é:", salfinal)
fimalgoritmo
