CREATE DATABASE IF NOT EXISTS Cancha_Libre;
USE Cancha_Libre;

-- 1. Tablas de Referencia (Maestros)
-- Primero las que no dependen de nadie

CREATE TABLE IF NOT EXISTS rol_pos (
    id_rol_pos INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE -- Ej: 'Arquero', 'Defensa', 'Ataque'
);

CREATE TABLE IF NOT EXISTS Posicion (
    id_pos INT AUTO_INCREMENT PRIMARY KEY,
    nombre_pos VARCHAR(50) NOT NULL, -- Ej: 'Central', 'Lateral', 'Enganche'
    id_rol_pos INT,
    FOREIGN KEY (id_rol_pos) REFERENCES rol_pos(id_rol_pos)
);

-- 2. Tablas de Entidades Principales

CREATE TABLE IF NOT EXISTS Usuario (
    id_u INT AUTO_INCREMENT PRIMARY KEY,
    nombre_c VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE, -- Agregué email para el login
    sexo BOOLEAN -- TRUE: Masculino, FALSE: Femenino (o viceversa)
);

CREATE TABLE IF NOT EXISTS Jugador (
    id_j INT AUTO_INCREMENT PRIMARY KEY,
    id_u_creador INT, -- El usuario que "dueño" de este contacto
    nombre_c VARCHAR(100) NOT NULL,
    sexo BOOLEAN,
    skill INT DEFAULT 5, -- Nivel del 1 al 10 para el matchmaking
    FOREIGN KEY (id_u_creador) REFERENCES Usuario(id_u) ON DELETE CASCADE
);

-- 3. Tablas Intermedias (Relaciones N:M)
-- Aquí definimos qué posiciones prefiere cada uno

CREATE TABLE IF NOT EXISTS Usuario_Posicion (
    id_u INT,
    id_pos INT,
    id_u_p INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (id_u) REFERENCES Usuario(id_u) ON DELETE CASCADE,
    FOREIGN KEY (id_pos) REFERENCES Posicion(id_pos)
);

CREATE TABLE IF NOT EXISTS Jugador_Posicion (
    id_j INT,
    id_pos INT,
    id_j_p INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (id_j) REFERENCES Jugador(id_j) ON DELETE CASCADE,
    FOREIGN KEY (id_pos) REFERENCES Posicion(id_pos)
);