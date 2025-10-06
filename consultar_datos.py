import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()

# Abrir archivo para escribir resultados
with open("reporte_estudiantes.txt", "w") as archivo:

    # 1. Consultar todos los registros
    archivo.write("--- Todos los estudiantes ---\n")
    print("\n--- Todos los estudiantes ---")
    cursor.execute("SELECT * FROM Estudiantes")
    for fila in cursor.fetchall():
        print(fila)                # Muestra en consola
        archivo.write(f"{fila}\n") # Guarda en archivo

    # 2. Filtrar estudiantes por ciudad
    archivo.write("\n--- Estudiantes de Bogotá ---\n")
    print("\n--- Estudiantes de Bogotá ---")
    cursor.execute("SELECT * FROM Estudiantes WHERE ciudad = 'Bogotá'")
    for fila in cursor.fetchall():
        print(fila)
        archivo.write(f"{fila}\n")

    # 3. Estudiantes mayores de 20 años
    archivo.write("\n--- Estudiantes mayores de 20 años ---\n")
    print("\n--- Estudiantes mayores de 20 años ---")
    cursor.execute("SELECT * FROM Estudiantes WHERE edad > 20")
    for fila in cursor.fetchall():
        print(fila)
        archivo.write(f"{fila}\n")

print("\n✅ Reporte generado en 'reporte_estudiantes.txt'.")

# Cerrar conexión
conexion.close()
