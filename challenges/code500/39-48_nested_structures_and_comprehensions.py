# ========================================
# === 039: crear_lista_diccionarios ===
# ========================================
print("Desafío 039")

"""
📌 CHALLENGE #039: crear_lista_diccionarios
- Crear una lista de diccionarios con datos de 3 estudiantes.
- Cada estudiante debe tener nombre, edad y lista de calificaciones.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""

students = [
    {"nombre": "Luis", "edad": 22, "calificaciones": [90, 85, 87]},
    {"nombre": "Jacob", "edad": 25, "calificaciones": [95, 97, 88]},
    {"nombre": "Nicole", "edad": 24, "calificaciones": [89, 94, 97]},
]

# ========================================
# === 040: calcular_promedio_estudiante ===
# ========================================
print("Desafío 040")

"""
📌 CHALLENGE #040: calcular_promedio_estudiante
- Calcular el promedio de calificaciones del segundo estudiante.
- Usa la lista de estudiantes del ejercicio 039.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""

def calcular_promedio_estudiante(student):
    avg = 0
    for calificacion in (students[student]["calificaciones"]):
        avg += calificacion
    avg /= len((students[student]["calificaciones"]))
    return avg

print(calcular_promedio_estudiante(2))

# ========================================
# === 041: agregar_calificacion ===
# ========================================
print("Desafío 041")

"""
📌 CHALLENGE #041: agregar_calificacion
- Agregar una nueva calificación a todos los estudiantes.
- Añade un número a la lista de calificaciones de cada estudiante.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""

def agregar_calificacion(grade):
    for student in students:
        student["calificaciones"].append(grade)
    return student["calificaciones"]

print(agregar_calificacion(100))


# ========================================
# === 042: crear_diccionario_materias ===
# ========================================
print("Desafío 042")

"""
📌 CHALLENGE #042: crear_diccionario_materias
- Crear un diccionario donde la clave sea una materia y el valor una lista de estudiantes inscritos.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""

subjects = {
    "math": ["Jacob", "Nicole", "Rosa", "Laura", "Joshua"]
}

# ========================================
# === 043: nombres_estudiantes_mayores_20 ===
# ========================================
print("Desafío 043")

"""
📌 CHALLENGE #043: nombres_estudiantes_mayores_20
- Usar comprensión de listas para obtener los nombres de estudiantes mayores de 20.
- Usa la lista del ejercicio 039.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""

mayores_de_20 = [est["nombre"] for est in students if est["edad"] > 20]

print(mayores_de_20)

# ========================================
# === 044: diccionario_promedios ===
# ========================================
print("Desafío 044")

"""
📌 CHALLENGE #044: diccionario_promedios
- Crear un diccionario que asocie cada nombre con su promedio.
- Usa la lista del ejercicio 039.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""
# Tu código aquí

# ========================================
# === 045: filtrar_estudiantes_promedio ===
# ========================================
print("Desafío 045")

"""
📌 CHALLENGE #045: filtrar_estudiantes_promedio
- Filtrar diccionarios de una lista para incluir solo a estudiantes con promedio mayor a 85.
- Usa la lista del ejercicio 039.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""
# Tu código aquí

# ========================================
# === 046: aplanar_lista_de_listas ===
# ========================================
print("Desafío 046")

"""
📌 CHALLENGE #046: aplanar_lista_de_listas
- Usar comprensión de listas para aplanar una lista de listas.

🧠 Ejemplo:
Entrada: [[10, 9], [8, 7], [6]]
Salida esperada: [10, 9, 8, 7, 6]
"""
# Tu código aquí

# ========================================
# === 047: contar_estudiantes_calificacion ===
# ========================================
print("Desafío 047")

"""
📌 CHALLENGE #047: contar_estudiantes_calificacion
- Crear una función que cuente cuántos estudiantes tienen al menos una calificación mayor a 90.

🧠 Ejemplo:
Entrada: ...
Salida esperada: ...
"""
# Tu código aquí

# ========================================
# === 048: diccionario_invertido ===
# ========================================
print("Desafío 048")

"""
📌 CHALLENGE #048: diccionario_invertido
- Crear un diccionario invertido a partir de un diccionario dado.

🧠 Ejemplo:
Entrada: {"a": 1, "b": 2, "c": 3}
Salida esperada: {1: "a", 2: "b", 3: "c"}
"""
# Tu código aquí
