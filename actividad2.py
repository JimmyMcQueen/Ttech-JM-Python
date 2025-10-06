import sqlite3

try:
    # 1. Conectar (o crear) la base de datos
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    print("Conexión a la base de datos establecida.")

    # 2. Eliminar la tabla si ya existe (evita duplicados)
    cursor.execute("DROP TABLE IF EXISTS Estudiantes")

    # 3. Crear tabla Estudiantes
    cursor.execute("""
    CREATE TABLE Estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER CHECK(edad > 0),
        ciudad TEXT
    )
    """)
    print("Tabla 'Estudiantes' creada con éxito.")

    # 4. Insertar datos básicos
    estudiantes = [
        ("Juan", 20, "Bogotá"),
        ("Ana", 22, "Medellín"),
        ("Luis", 19, "Cali"),
        ("María", 25, "Bogotá"),
    ]

    cursor.executemany(
        "INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES (?, ?, ?)", 
        estudiantes
    )
    conexion.commit()
    print("Datos insertados en la tabla.")

    # 5. Consultar todos los registros
    print("\n--- Todos los estudiantes ---")
    cursor.execute("SELECT * FROM Estudiantes")
    filas = cursor.fetchall()
    if filas:
        for fila in filas:
            print(fila)
    else:
        print("No hay registros en la tabla.")

    # 6. Filtrar estudiantes por ciudad
    ciudad = "Bogotá"
    print(f"\n--- Estudiantes de {ciudad} ---")
    cursor.execute("SELECT * FROM Estudiantes WHERE ciudad = ?", (ciudad,))
    filas = cursor.fetchall()
    if filas:
        for fila in filas:
            print(fila)
    else:
        print(f"No se encontraron estudiantes en {ciudad}.")

    # 7. Consultar estudiantes mayores de 20 años
    print("\n--- Estudiantes mayores de 20 años ---")
    cursor.execute("SELECT * FROM Estudiantes WHERE edad > 20")
    filas = cursor.fetchall()
    if filas:
        for fila in filas:
            print(fila)
    else:
        print("No hay estudiantes mayores de 20 años.")

except sqlite3.Error as e:
    print("Error en la base de datos:", e)

finally:
    if conexion:
        conexion.close()
        print("\n Conexión cerrada correctamente.")
