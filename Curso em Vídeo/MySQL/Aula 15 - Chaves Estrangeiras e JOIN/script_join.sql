USE cadastro;
select * from gafanhotos;
SELECT nome, cursopreferido FROM gafanhotos;

SELECT nome, ano FROM cursos;

-- JOIN - Comando que junta une duas tabelas mostrando os que tem corrêspondecias (Default é INNER JOIN)
-- INNER JOIN - Funciona como o JOIN, apenas forma alternativa de escrita
-- ON - Indica a relação entre 2 tabelas no JOIN
SELECT gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano 
FROM gafanhotos JOIN cursos
ON cursos.idcurso = gafanhotos.cursopreferido;

-- AS - Usado para apelidar colunas
SELECT g.nome, g.cursopreferido, c.nome, c.ano 
FROM gafanhotos AS g JOIN cursos AS c
ON c.idcurso = g.cursopreferido;

-- OUTER JOIN - Junta as tabelas e inclui os registros sem correspondências
-- LEFT - Da preferência de exibição para a tabela da esquerda (Default é OUTER)
SELECT g.nome, g.cursopreferido, c.nome, c.ano 
FROM gafanhotos AS g LEFT OUTER JOIN cursos AS c
ON c.idcurso = g.cursopreferido;

SELECT g.nome, g.cursopreferido, c.nome, c.ano 
FROM gafanhotos AS g LEFT JOIN cursos AS c -- Sem incluir a palavra OUTER
ON c.idcurso = g.cursopreferido;

-- RIGHT - Da preferência de exibição para a tabela da direita (Default é OUTER)
SELECT g.nome, g.cursopreferido, c.nome, c.ano 
FROM gafanhotos AS g RIGHT JOIN cursos AS c
ON c.idcurso = g.cursopreferido;