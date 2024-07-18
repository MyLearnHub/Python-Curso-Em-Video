USE cadastro;

SELECT * FROM cursos WHERE nome = 'PHP'; -- Seleção por nome

-- LIKE - É um operador de comparação que identifica algo 'parecido', se contém aquele conteúdo
SELECT * FROM cursos WHERE nome LIKE 'P%'; -- % - Indica que o que vem depois é irrelevante

SELECT * FROM cursos WHERE nome LIKE '%A'; -- Buscando nomes terminados com a letra 'A' 

SELECT * FROM cursos WHERE nome LIKE '%A%'; -- Buscando nomes que contenham a letra 'A' 

-- NOT - Nega a condição desejada
SELECT * FROM cursos WHERE nome NOT LIKE '%A%'; 

SELECT * FROM cursos WHERE nome LIKE 'PH%P'; -- Buscando qualquer coisa com começo e fim

SELECT * FROM cursos WHERE nome LIKE 'PH%P_'; -- _ - Exige que tenha um caractere no espaço

SELECT * FROM cursos WHERE nome LIKE 'P_P%'; -- Utilizando buscador de caractere e buscador de qualquer

SELECT * FROM cursos WHERE nome LIKE 'P__T%'; -- Buscando 2 caracteres qualquer

SELECT * FROM gafanhotos WHERE nome LIKE '%SILVA%'; -- Buscando pessoas com 'SILVA' no nome

-- DISTINCT - Mostra todas as ocorrências eliminando as que se repetem
SELECT DISTINCT carga FROM cursos ORDER BY carga;

SELECT DISTINCT nacionalidade FROM gafanhotos ORDER BY nacionalidade;

-- COUNT() - Função que realiza uma contagem
SELECT COUNT(nome) FROM cursos;

SELECT COUNT(*) FROM cursos;

SELECT COUNT(*) FROM cursos WHERE carga > '40'; -- Conta os cursos com carga horária maior que 40

-- MAX() - Função que pega o valor máximo
SELECT MAX(totaulas) FROM cursos;

SELECT MAX(carga) FROM cursos WHERE ano = '2016';

-- MIN() - Função que pega o valor mínimo
SELECT MIN(totaulas) FROM cursos;

SELECT nome, MIN(totaulas) FROM cursos WHERE ano = '2016'; -- Aqui talvez possa dar erro, use o comando: SET sql_mode = '' para desabilitar a validação SQL temporariamente

-- SUM() - Função que soma os valores
SELECT SUM(totaulas) FROM cursos;

-- AVG() - Função que tira a média entre os valores
SELECT AVG(totaulas) FROM cursos;