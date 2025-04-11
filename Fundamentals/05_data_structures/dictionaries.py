# ========================================
# Uso de Diccionarios en Python
# ========================================

"""
## 📌 Descripción
Un diccionario en Python es una estructura de datos que almacena información en pares **clave-valor**.

📌 **Características principales:**
- Las claves deben ser únicas e inmutables (por ejemplo: strings, números, tuplas).
- Los valores pueden ser de cualquier tipo.
- Los diccionarios son **mutables**, es decir, se pueden modificar después de su creación.
- Se accede a los valores usando la clave (no con índices como en las listas).

📌 Sintaxis básica:
    mi_diccionario = {
        'clave1': valor1,
        'clave2': valor2
    }

"""

# ========================================
# Ejemplo básico de diccionario
# ========================================

persona = {
    "nombre": "Jacob",
    "edad": 28,
    "ciudad": "Santiago"
}

print(persona["nombre"])  # Accede al valor de la clave "nombre"

# ========================================
# Agregar, modificar y eliminar elementos
# ========================================

# Agregar una nueva clave
persona["profesion"] = "Desarrollador"

# Modificar el valor de una clave existente
persona["edad"] = 29

# Eliminar una clave
del persona["ciudad"]

print(persona)

# ========================================
# Iterar sobre un diccionario
# ========================================

"""
Podemos iterar sobre claves, valores o ambos con métodos específicos:
- .keys() → devuelve todas las claves
- .values() → devuelve todos los valores
- .items() → devuelve tuplas (clave, valor)
"""

for clave in persona.keys():
    print(f"Clave: {clave}")

for valor in persona.values():
    print(f"Valor: {valor}")

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# ========================================
# Comprobar si una clave existe
# ========================================

if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario.")

# ========================================
# Métodos útiles de diccionarios
# ========================================

"""
- .get(clave, valor_por_defecto): devuelve el valor de una clave, o el valor por defecto si no existe.
- .pop(clave): elimina una clave y devuelve su valor.
- .clear(): elimina todos los elementos.
"""

print(persona.get("nombre", "Desconocido"))  # "Jacob"
print(persona.get("altura", "No especificada"))  # Valor por defecto

# ========================================
# Diccionarios anidados
# ========================================

"""
Podemos tener diccionarios dentro de diccionarios (estructura anidada).
"""

estudiantes = {
    "Juan": {"edad": 20, "carrera": "Ingeniería"},
    "Ana": {"edad": 22, "carrera": "Medicina"}
}

print(estudiantes["Ana"]["carrera"])  # Accede al valor anidado

# ========================================
# Resumen
# ========================================

"""
## 📌 Resumen

- Un diccionario almacena datos en pares clave-valor.
- Se accede a los valores usando su clave.
- Las claves deben ser únicas y de tipo inmutable.
- Los valores pueden ser de cualquier tipo.
- Métodos comunes: .get(), .pop(), .keys(), .values(), .items()
- Pueden usarse dentro de estructuras anidadas para representar datos complejos.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica para diccionarios

Resuelve los siguientes ejercicios para practicar la creación, acceso y manipulación de diccionarios.
"""

# --------------------------------------------------
# 1️⃣ Crea un diccionario con los datos de una persona: nombre, edad y país
# --------------------------------------------------

persona = {
    "nombre": "",
    "edad": 0,
    "país": ""
}

# --------------------------------------------------
# 2️⃣ Agrega una clave "profesión" con cualquier valor
# --------------------------------------------------

persona["profesión"] = ""

# --------------------------------------------------
# 3️⃣ Modifica el valor de "edad"
# --------------------------------------------------

persona["edad"] = 30  # Cambia 30 por la edad deseada

# --------------------------------------------------
# 4️⃣ Verifica si la clave "nombre" está en el diccionario e imprímela
# --------------------------------------------------

if "nombre" in persona:
    print(persona["nombre"])

# --------------------------------------------------
# 5️⃣ Elimina la clave "país" y muestra el diccionario resultante
# --------------------------------------------------

del persona["país"]
print(persona)

# --------------------------------------------------
# 6️⃣ Crea un diccionario de estudiantes con nombres como claves y otro diccionario como valor (edad y carrera)
# --------------------------------------------------

estudiantes = {
    "Carlos": {"edad": 21, "carrera": "Arquitectura"},
    "Laura": {"edad": 23, "carrera": "Biología"}
}

# --------------------------------------------------
# 7️⃣ Accede al valor "carrera" del estudiante "Juan"
# --------------------------------------------------

print(estudiantes["Carlos"]["carrera"])  # Cambia "Carlos" por "Juan" si lo deseas

# ========================================
# Fin del Documento
# ========================================
