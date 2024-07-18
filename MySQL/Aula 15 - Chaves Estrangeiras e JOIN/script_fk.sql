USE cadastro;

ALTER TABLE gafanhotos ADD cursopreferido INT;

-- FOREIGN KEY - Indica que a coluna será uma chave estrangeira
-- REFERENCES - Referência a chave da outra tabela
ALTER TABLE gafanhotos ADD FOREIGN KEY (cursopreferido) REFERENCES cursos(idcurso);

UPDATE gafanhotos SET cursopreferido = '6' WHERE id = '1'; -- Atualizando a chave estrangeira

DELETE FROM cursos WHERE idcurso = '28'; -- Esse delete funciona pois não se relaciona com nenhuma outra tupla