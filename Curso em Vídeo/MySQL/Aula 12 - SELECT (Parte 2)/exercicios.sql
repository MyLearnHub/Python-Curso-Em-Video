USE cadastro;

-- Exercício 1 - Uma lista com o nome de todas as gafanhotas
SELECT nome FROM gafanhotos WHERE sexo = 'F';

-- Exercício 2 - Uma lista com os dados de todos aqueles que nasceram entre 1/Jan/2000 e 31/Dez/2015
SELECT * FROM gafanhotos WHERE nascimento BETWEEN '2000-01-01' AND '2015-12-31';

-- Exercício 3 - Uma lista com o nome de todos os homens que trabalham como Programadores
SELECT nome FROM gafanhotos WHERE sexo = 'M' AND profissao = 'Programador';

-- Exercício 4 - Uma lista com todos os dados de todas as mulheres que nasceram no Brasil e que têm seu nome iniciado com a letra J
SELECT * FROM gafanhotos WHERE sexo = 'F' AND nacionalidade = 'Brasil' AND nome LIKE 'J%';

-- Exercício 5 - Uma lista com o nome e nacionalidade de todos os homens que têm Silva no nome, não nasceram no Brasil e pesam menos de 100 Kg
SELECT nome, nacionalidade FROM gafanhotos WHERE sexo = 'M' AND nome LIKE '%Silva%' AND nacionalidade <> 'Brasil' AND peso < '100';

-- Exercício 6 - Qual é a maior altura entre gafanhotos homens que moram no Brasil?
SELECT MAX(altura) FROM gafanhotos WHERE sexo = 'M' AND nacionalidade = 'Brasil';

-- Exercício 7 - Qual é a média de peso dos gafanhotos cadastrados?
SELECT AVG(peso) FROM gafanhotos;

-- Exercício 8 - Qual é o menor peso entre as gafanhotos mulheres que nasceram fora do Brasil e entre 01/Jan/1990 e 31/Dez/2000?
SELECT MIN(peso) FROM gafanhotos WHERE sexo = 'F' AND nacionalidade <> 'Brasil' AND nascimento BETWEEN '1990-01-01' AND '2000-12-31';

-- Exercício 9 - Quantas gafanhotos mulheres têm mais de 1.90m de altura?
SELECT COUNT(*) FROM gafanhotos WHERE sexo = 'F' AND altura > '1.90';