var s = "JavaScript";
console.log(s);

console.log("Eu estou estudando s");
console.log("Eu estou estudando " + s);

nome = "Gustavo";
idade = 41;
nota = 5.5;

console.log("O aluno" + nome + "com" + idade + "anos tirou a nota" + nota);
console.log(`O aluno ${nome} com ${idade} anos tirou a nota ${nota}`);

var n1 = 1545.5;
console.log(n1);

console.log(n1.toFixed(2));
console.log(n1.toFixed(2).replace(".", ","));
console.log(n1.toLocaleString("pt-BR", { style: "currency", currency: "BRL" }));
console.log(n1.toLocaleString("pt-BR", { style: "currency", currency: "USD" }));
console.log(n1.toLocaleString("pt-BR", { style: "currency", currency: "EUR" }));
