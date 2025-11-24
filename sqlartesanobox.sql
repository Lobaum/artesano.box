CREATE DATABASE artesano;
USE artesano;

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(120) NOT NULL,
  email VARCHAR(120) NOT NULL UNIQUE,
  senha VARCHAR(255) NOT NULL,
  tipo_conta ENUM('artesao','cliente') NOT NULL
);

SELECT * FROM usuarios;