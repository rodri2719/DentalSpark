import sqlite3

# Crear base de datos y tabla de usuarios en registros.sql
conn = sqlite3.connect('registros.sql')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    correo TEXT UNIQUE NOT NULL,
    contrasena TEXT NOT NULL
)''')

# Insertar usuario predeterminado
correo = 'rodrigodurazno238@gmail.com'
contrasena = 'Rodri27021915'
try:
    c.execute("INSERT INTO usuarios (correo, contrasena) VALUES (?, ?)", (correo, contrasena))
    conn.commit()
    print('Usuario creado correctamente en registros.sql.')
except sqlite3.IntegrityError:
    print('El usuario ya existe en registros.sql.')

conn.close()
