-- CREATE DATABASE - Cria um Banco de Dados
-- USE - Usa o Banco de Dados
CREATE DATABASE cadastro;
USE cadastro;

-- CREATE TABLE - Cria uma nova tabela
CREATE TABLE pessoas (
	nome VARCHAR(30),
    idade TINYINT,
    sexo CHAR(1),
    peso FLOAT,
    altura FLOAT,
    nacionalidade VARCHAR(20)
);
