USE cadastro;

-- IF NOT EXISTS - Só realiza o comando se não existir 
CREATE TABLE IF NOT EXISTS cursos (
    nome VARCHAR(30) NOT NULL UNIQUE,
    descricao TEXT,
    carga INT UNSIGNED,
    totaulas INT,
    ano YEAR DEFAULT '2016'
) DEFAULT CHARSET = utf8mb4 ;

ALTER TABLE cursos 
ADD COLUMN idcurso INT FIRST;

-- Adicionando chave primária depois da criação da tabela
ALTER TABLE cursos 
ADD PRIMARY KEY (idcurso);

CREATE TABLE IF NOT EXISTS teste (
	id INT,
    nome VARCHAR(10),
    idade INT
);

INSERT INTO teste VALUES
('1', 'Pedro', '22'),
('2', 'Maria', '12'),
('3', 'Maricota', '77');

-- DROP TABLE - Exclui a tabela
-- IF EXISTS - Só realiza o comando se existir 
DROP TABLE IF EXISTS teste;