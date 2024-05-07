algoritmo "Sistema de login triplo"
// Função : Conferir senha e usuário
// Autor : Paulo Alvares
// Data : 06/01/2023
// Seção de Declarações
var
   usuario, senha : caractere
inicio
   escreva("Digite seu nome de usuário:")
   leia(usuario)
   escreva("Digite sua senha:")
   leia(senha)
   se (usuario = "admin") e (senha = "123") ou (usuario = "suporte") e (senha = "456") ou (usuario = "Aluno") e (senha = "999") entao
      escreva("Acesso permitido")
   senao
      escreva("Acesso negado")
   fimse
fimalgoritmo
