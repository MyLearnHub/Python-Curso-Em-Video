USE cadastro;

-- GROUP BY - Agrupa os elementos a serem exibidos
SELECT carga FROM cursos GROUP BY carga; -- Parece semelhante ao DISTINCT mas ele é semânticamente diferente

SELECT carga, COUNT(nome) FROM cursos GROUP BY carga; -- Utilizando o COUNT() dá pra saber a quantidade de cada registro

SELECT totaulas, COUNT(*) FROM cursos GROUP BY totaulas ORDER BY totaulas;

-- HAVING - Tupla que possui algo
SELECT carga, COUNT(nome) FROM cursos GROUP BY carga HAVING COUNT(nome) > '3';

SELECT ano, COUNT(*) FROM cursos GROUP BY ano HAVING COUNT(ano) >= '5' ORDER BY COUNT(*) DESC;

SELECT ano, COUNT(*) FROM cursos WHERE totaulas > '30' GROUP BY ano HAVING ano > '2013' ORDER BY COUNT(*) DESC; -- Selecionando, filtrando e agrupando

SELECT carga, COUNT(*) FROM cursos WHERE ano > '2015' GROUP BY carga HAVING carga > (SELECT AVG(carga) FROM cursos); -- Comparando um SELECT com o outro