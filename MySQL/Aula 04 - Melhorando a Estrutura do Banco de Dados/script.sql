-- DROP DATABASE - Exclui o Banco de Dados
DROP DATABASE cadastro;

-- DEFAULT CHARACTER SET - Indica o padrão de caracteres do Banco de Dados
-- DEFAUL COLLATE - Indica o padrão de coleções do Banco de Dados
CREATE DATABASE cadastro 
DEFAULT CHARACTER SET utf8mb4 		-- O padrão do curso (utf8) foi depreciado
DEFAULT COLLATE utf8mb4_general_ci; -- O padrão do curso (utf8_general_ci) foi depreciado

USE cadastro;

CREATE TABLE pessoas (
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(30) NOT NULL,
    nascimento DATE,
    sexo ENUM('M', 'F'),
    peso DECIMAL(5,2),
    altura DECIMAL(3,2),
    nacionalidade VARCHAR(20) DEFAULT 'Brasil',
	PRIMARY KEY(id)
) DEFAULT CHARSET = utf8mb4;