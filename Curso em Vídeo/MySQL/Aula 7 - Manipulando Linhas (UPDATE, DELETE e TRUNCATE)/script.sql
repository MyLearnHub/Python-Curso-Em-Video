USE cadastro;

INSERT INTO cursos VALUES
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica de Programação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução à linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('9', 'Cozinha Árabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
('10', 'YouTuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

SELECT * FROM cursos;

-- UPDATE - Atualiza uma tabela
-- SET - Indica um novo valor a um campo
-- WHERE - Indica onde a alteração deve acontecer
UPDATE cursos 
SET nome = 'HTML5' 
WHERE idcurso = 1;

UPDATE cursos 
SET nome = 'PHP', ano = '2015' -- Incluir a vírgula altera multiplas colunas
WHERE idcurso = 4;

-- LIMIT - Limita as alterações para afetar apenas a quantidade de linhas desejada
UPDATE cursos 
SET nome = 'Java', carga = '40', ano = '2015'
WHERE idcurso = 5
LIMIT 1;

-- DELETE FROM - Deleta algo de uma tabela
DELETE FROM cursos
WHERE idcurso = '8';

DELETE FROM cursos
WHERE ano = '2018' -- Afetar multíplos campos
LIMIT 3;

-- TRUNCATE TABLE - Elimina todas as linhas da tabela
-- Também funciona resumindo o código - TRUNCATE cursos;
TRUNCATE TABLE cursos;