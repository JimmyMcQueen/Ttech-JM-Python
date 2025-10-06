from pymongo import MongoClient

# Conectar a MongoDB (local)
# Si usas Atlas, aquí va la cadena de conexión que te da la nube
cliente = MongoClient("mongodb://localhost:27017/")

# Crear base de datos y colección
db = cliente["mi_base"]
coleccion = db["Estudiantes"]

# Limpiar colección antes de insertar (para evitar duplicados si ejecutas varias veces)
coleccion.delete_many({})

# Insertar documentos
estudiantes = [
    {"nombre": "Juan", "edad": 20, "ciudad": "Bogotá"},
    {"nombre": "Ana", "edad": 22, "ciudad": "Medellín"},
    {"nombre": "Luis", "edad": 19, "ciudad": "Cali"}
]

coleccion.insert_many(estudiantes)
print(" Documentos insertados en la colección 'Estudiantes'.")
# 1. Consultar todos los documentos
print("\n--- Todos los estudiantes ---")
for estudiante in coleccion.find():
    print(estudiante)

# 2. Filtrar estudiantes por ciudad
print("\n--- Estudiantes de Bogotá ---")
for estudiante in coleccion.find({"ciudad": "Bogotá"}):
    print(estudiante)

# 3. Estudiantes mayores de 20 años
print("\n--- Estudiantes mayores de 20 años ---")
for estudiante in coleccion.find({"edad": {"$gt": 20}}):
    print(estudiante)
