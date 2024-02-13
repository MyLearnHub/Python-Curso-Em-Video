USE cadastro;

-- DESCRIBE - Descreve as colunas de uma tabela
-- DESC - Comando DESCRIBE resumido
DESCRIBE pessoas;
DESC pessoas;

-- ALTER TABLE - Altera algo em uma tabela
-- ADD COLUMN - Adiciona uma coluna nova a tabela
ALTER TABLE pessoas 
ADD COLUMN profissao VARCHAR(10);

-- DROP COLUMN - Elimina uma coluna da tabela
ALTER TABLE pessoas 
DROP COLUMN profissao;

-- AFTER - Especifica a adição da nova coluna após outra coluna existente
ALTER TABLE pessoas 
ADD COLUMN profissao VARCHAR(10) AFTER nome;

-- FIRST - Adiciona a nova coluna como primeira da tabela
-- Esses comandos podem ou não conter a palavra COLUMN
ALTER TABLE pessoas 
ADD codigo INT FIRST;

-- MODIFY COLUMN - Modifica alguma característica da coluna
ALTER TABLE pessoas 
MODIFY COLUMN profissao VARCHAR(20) NOT NULL DEFAULT '';

-- CHANGE COLUMN - Altera o nome da coluna
ALTER TABLE pessoas
CHANGE COLUMN profissao prof VARCHAR(20) DEFAULT '';

-- RENAME TO - Renomeia a tabela
ALTER TABLE pessoas
RENAME TO gafanhotos;