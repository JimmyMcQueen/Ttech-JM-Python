# Paso 1
# Programa que imprime un mensaje
print("¡Hola, bienvenido a Fundamentos de Python!")
# Variables de distintos tipos
numero_entero = 10          # int
numero_decimal = 3.5        # float
texto = "Python"            # str

# Operaciones matemáticas
suma = numero_entero + numero_decimal
resta = numero_entero - numero_decimal
multiplicacion = numero_entero * numero_decimal
division = numero_entero / numero_decimal

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Concatenación de cadenas
nombre = "Jaime"
saludo = "Hola " + nombre + ", ¡bienvenido a Python!"
print(saludo)

# Uso de input()
usuario = input("¿Cuál es tu lenguaje de programación favorito?: ")
print("Tu lenguaje favorito es: " + usuario)


# Paso 2
# Pedir un número al usuario
numero = int(input("Ingresa un número: "))

# Condicional para verificar si es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es PAR")
else:
    print(f"El número {numero} es IMPAR")

# Lista de números
numeros = [1, 2, 3, 4, 5]

print("Los cuadrados de los números son:")

# Recorremos la lista
for n in numeros:
    print(f"{n}² = {n**2}")

# Pedir repetidamente un número hasta que sea mayor que 10
numero = 0  # valor inicial

while numero <= 10:
    numero = int(input("Ingresa un número mayor que 10: "))

print(f"¡Perfecto! Ingresaste {numero}, que es mayor que 10.")


# Paso 3
# Lista de nombres de estudiantes
estudiantes = ["Jaime", "Luis", "María", "Carlos"]

print("Lista de estudiantes:")
for nombre in estudiantes:
    print(nombre)

# Diccionario con información de contacto
contacto = {
    "nombre": "Jaime Cuellar",
    "correo": "jaime.c@email.com"
}

print("Información de contacto:")

# Recorrer claves y valores del diccionario
for clave, valor in contacto.items():
    print(clave, ":", valor)

# Lista y diccionario iniciales
estudiantes = ["Jaime", "Luis"]
contacto = {"nombre": "Jaime Cuellar", "correo": "jaime.c@email.com"}

opcion = 0

while opcion != 3:
    print("\nMenú:")
    print("1. Agregar estudiante a la lista")
    print("2. Actualizar información de contacto")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print("Lista actualizada:", estudiantes)

    elif opcion == 2:
        clave = input("¿Qué deseas actualizar (nombre/correo)?: ")
        valor = input(f"Ingresa el nuevo {clave}: ")
        contacto[clave] = valor
        print("Contacto actualizado:", contacto)

    elif opcion == 3:
        print("Saliendo del programa...")

    else:
        print("Opción inválida, intenta de nuevo.")


# Paso 4
print("=== Calculadora Básica ===")

while True:
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "5":
        print("Saliendo de la calculadora...")
        break

    # Pedir los números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif opcion == "2":
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif opcion == "3":
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif opcion == "4":
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Opción inválida. Intenta de nuevo.")


# === Juego de Adivinanza ===
import random

print("\n=== Juego de Adivinanza ===")
numero_secreto = random.randint(1, 100)  # Número aleatorio entre 1 y 100
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1

    if intento == numero_secreto:
        print(f"🎉 ¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intentos.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número secreto es MAYOR.")
    else:
        print("El número secreto es MENOR.")
