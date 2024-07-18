function contar() {
  let inicio = document.querySelector("input#inicio");
  let fim = document.querySelector("input#fim");
  let passo = document.querySelector("input#pass");
  let res = document.querySelector("div#res");

  if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0) {
    res.innerHTML = "Impossivel de contar!";
  } else {
    res.innerHTML = "Contando: <br>";

    let start = Number(inicio.value);
    let end = Number(fim.value);
    let salto = Number(passo.value);

    if (salto <= 0) {
      window.alert("Passo inválido! Considerando PASSO 1");
      salto = 1;
    }

    if (start < end) {
      for (var controle = start; controle <= end; controle += salto) {
        res.innerHTML += `${controle} 👉`;
      }
    } else {
      for (var contador = start; contador >= end; contador -= salto) {
        res.innerHTML += `${contador} 👉`;
      }
    }

    res.innerHTML += "🏴";
  }
}
