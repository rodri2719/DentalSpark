-- Script para crear la tabla de usuarios y un usuario por defecto

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    correo TEXT UNIQUE NOT NULL,
    contrasena TEXT NOT NULL
);

INSERT OR IGNORE INTO usuarios (correo, contrasena) VALUES ('rodrigodurazno238@gmail.com', 'Rodri27021915');
