USE cadastro;

INSERT INTO pessoas(nome, nascimento, sexo, peso, altura, nacionalidade) VALUES
('Godofredo', '1984-01-02', 'M', '78.5', '1.83', 'Brasil'),
('Maria', '1999-01-02', 'F', '55.2', '1.75', 'Portugal');

INSERT INTO pessoas(id, nome, nascimento, sexo, peso, altura, nacionalidade) VALUES
(DEFAULT, 'Creuza', '1920-12-30', 'F', '50.2', '1.65', DEFAULT);

INSERT INTO pessoas VALUES
(DEFAULT, 'Adalgiza', '1930-11-02', 'F', '63.2', '1.75', 'Irlanda'),
(DEFAULT, 'Ana', '1975-12-22', 'F', '52.3', '1.45', 'EUA'),
(DEFAULT, 'Pedro', '2000-07-15', 'M', '52.3', '1.45', 'Brasil'),
(DEFAULT, 'Maria', '1999-05-30', 'F', '75.9', '1.70', 'Portugal'),
(DEFAULT, 'Cláudio', '1975-04-22', 'M', '99.0', '2.15', 'Brasil'),
(DEFAULT, 'Pedro', '1999-12-03', 'M', '87', '2', DEFAULT),
(DEFAULT, 'Janaína', '1987-11-12', 'F', '75.4', '1.66', 'EUA');

SELECT * FROM pessoas;