Algoritmo "contagem-inteligente"
Var
  start, end: inteiro
Inicio
  escreval("----------------------")
  escreval(" CONTAGEM INTELIGÊNTE ")
  escreval("----------------------")
  escreva("Início:")
  leia(start)
  escreva("Fim:")
  leia(end)
  
  escreval("----------------------")
  escreval("       CONTANDO       ")
  escreval("----------------------")

  se (start > end) entao
    enquanto (start >= end) faca
      escreva(start, "...")
      start <- start - 1
    fimenquanto
  senao
    enquanto (start <= end) faca
      escreva(start, "...")
      start <- start + 1
    fimenquanto
  fimse
Fimalgoritmo