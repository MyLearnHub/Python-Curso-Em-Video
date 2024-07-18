USE cadastro;

-- ORDER BY - Ordena o select (O Default é por ordem alfabetica)
SELECT * FROM cursos ORDER BY nome;

-- DESC - Especifica a ordenação em ordem decrescente
SELECT * FROM cursos ORDER BY nome DESC;

-- ASC - Especifica a ordenação em ordem crescente
SELECT * FROM cursos ORDER BY nome ASC;

SELECT nome, carga, ano FROM cursos ORDER BY nome; -- Especificando os campos desejados

SELECT ano, nome, carga FROM cursos ORDER BY ano; -- Alterando a ordem de mostragem

SELECT ano, nome, carga FROM cursos ORDER BY ano, nome; -- Especificando a ordem de mostragem

SELECT * FROM cursos WHERE ano = '2016' ORDER BY nome; -- Selecionando valores especificos

SELECT nome, carga FROM cursos WHERE ano = '2016' ORDER BY nome; -- Especificando campos e selecionando valores especificos

SELECT nome, descricao, ano FROM cursos WHERE ano <= '2015' ORDER BY ano, nome; -- Utilizando operadores na consulta

SELECT nome, descricao, ano FROM cursos WHERE ano > '2016' ORDER BY ano, nome; -- Utilizando operador de maior

SELECT nome, descricao, ano FROM cursos WHERE ano != '2017' ORDER BY ano, nome; -- Utilizando operador de diferente (Também funciona assim: <>)

-- BETWEEN - Especifica um intervalo
-- AND - Define uma adição a condição
SELECT * FROM cursos WHERE totaulas BETWEEN '20' AND '30' ORDER BY nome;

SELECT nome, ano FROM cursos WHERE ano BETWEEN '2014' AND '2016' ORDER BY ano DESC, nome ASC; -- Especificando parâmetros na ordem de apresentação

-- IN - Define valores especificos
SELECT idcurso, nome FROM cursos WHERE ano IN('2014', '2016', '2018') ORDER BY nome; 

SELECT * FROM cursos WHERE carga > '35' AND totaulas < '30' ORDER BY nome; -- Usando duas colunas como condição

-- OR - Operador relacional de condição (Ou)
SELECT nome, carga, totaulas FROM cursos WHERE carga > '35' OR totaulas < '30' ORDER BY nome;