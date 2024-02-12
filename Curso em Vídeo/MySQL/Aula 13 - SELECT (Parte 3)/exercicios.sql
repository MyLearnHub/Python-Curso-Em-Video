USE cadastro;
select * from gafanhotos;
-- Exercício 1 - Uma lista com as profissões dos gafanhotos e seus respectivos quantitativos
SELECT profissao, COUNT(*) FROM gafanhotos GROUP BY profissao;

-- Exercício 2 - Quantos gafanhotos homens e quantas mulheres nasceram após 01/Jan/2005?
SELECT sexo, COUNT(*) FROM gafanhotos WHERE nascimento > '2005-01-01' GROUP BY sexo;

-- Exercício 3 - Uma lista com os gafanhotos que nasceram fora do Brasil, mostrando o país de origem
-- e o total de pessoas nascidas lá. Só nos interessam os países que tiverem mais de 3 gafanhotos com essa nacionalidade
SELECT nacionalidade, COUNT(*) FROM gafanhotos WHERE nacionalidade <> 'Brasil' GROUP BY nacionalidade HAVING COUNT(*) > '3';

-- Exercício 4 - Uma lista agrupada pela altura dos gafanhotos, mostrando quantas pessoas pesam mais de 100Kg 
-- e que estão acima da média de altura de todos os cadastrados
SELECT altura, COUNT(*) FROM gafanhotos WHERE peso > '100' AND altura > (SELECT AVG(altura) FROM gafanhotos) GROUP BY altura;

