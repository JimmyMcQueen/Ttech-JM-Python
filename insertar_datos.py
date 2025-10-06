import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()

# Datos de ejemplo
estudiantes = [
    ("Juan", 20, "Bogotá"),
    ("Ana", 22, "Medellín"),
    ("Luis", 19, "Cali"),
    ("María", 25, "Bogotá"),
]

# Insertar datos
cursor.executemany("INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES (?, ?, ?)", estudiantes)
conexion.commit()

print("✅ Datos insertados con éxito.")

# Cerrar conexión
conexion.close()
