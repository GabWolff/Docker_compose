CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO usuarios (nome, email) VALUES
    ('Alice Silva', 'alice@email.com'),
    ('Bruno Costa', 'bruno@email.com'),
    ('Carla Mendes', 'carla@email.com');