import sqlite3

# Conectar (o crear) la base de datos
conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()

# Eliminar tabla si ya existe (para empezar limpio cada vez)
cursor.execute("DROP TABLE IF EXISTS Estudiantes")

# Crear la tabla
cursor.execute("""
CREATE TABLE Estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER,
    ciudad TEXT
)
""")

print(" Tabla 'Estudiantes' creada con éxito.")

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()
