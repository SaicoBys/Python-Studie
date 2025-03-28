

#!/usr/bin/env python3
# ========================================
# Introducción a Listas en Python
# ========================================

"""
## 📌 Descripción
Las listas (`list`) en Python son colecciones ordenadas y mutables.
Permiten almacenar múltiples valores en una sola variable y pueden contener diferentes tipos de datos.

📌 **Características principales de las listas**:
- **Ordenadas** → Mantienen el orden de inserción.
- **Mutables** → Sus elementos pueden modificarse.
- **Heterogéneas** → Pueden contener distintos tipos de datos (enteros, cadenas, listas, etc.).
"""

# ========================================
# 1. Creación de Listas
# ========================================

"""
Las listas se crean usando corchetes `[]` y separando los elementos con comas.
"""

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de cadenas
nombres = ["Ana", "Carlos", "Luis"]

# Lista mixta
mixta = [1, "Python", 3.14, True]

# Lista vacía
vacia = []

print(numeros)  # [1, 2, 3, 4, 5]
print(nombres)  # ['Ana', 'Carlos', 'Luis']
print(mixta)    # [1, 'Python', 3.14, True]
print(vacia)    # []

# ========================================
# 2. Acceso a Elementos
# ========================================

"""
Los elementos de una lista se acceden mediante índices (empezando en 0).
"""

print(nombres[0])  # Ana
print(nombres[-1])  # Luis (índice negativo)

# Modificación de elementos
nombres[1] = "Pedro"
print(nombres)  # ['Ana', 'Pedro', 'Luis']

# ========================================
# 3. Métodos Comunes de Listas
# ========================================

"""
Las listas tienen varios métodos para modificar su contenido.
"""

# `.append()` → Agrega un elemento al final
nombres.append("Marta")
print(nombres)  # ['Ana', 'Pedro', 'Luis', 'Marta']

# `.remove()` → Elimina la primera ocurrencia de un valor
nombres.remove("Pedro")
print(nombres)  # ['Ana', 'Luis', 'Marta']

# `.pop()` → Elimina y devuelve el último elemento (o uno específico)
ultimo = nombres.pop()
print(ultimo)  # 'Marta'
print(nombres)  # ['Ana', 'Luis']

# `.sort()` → Ordena la lista (solo funciona con datos del mismo tipo)
numeros.sort()
print(numeros)  # [1, 2, 3, 4, 5]

# `.reverse()` → Invierte el orden de la lista
numeros.reverse()
print(numeros)  # [5, 4, 3, 2, 1]

# `.index()` → Devuelve la posición de un elemento
print(nombres.index("Ana"))  # 0

# ========================================
# 4. Operaciones con Listas
# ========================================

"""
Las listas permiten operaciones como concatenación, repetición y verificación de pertenencia.
"""

# Concatenación de listas
nueva_lista = nombres + ["Sofía", "David"]
print(nueva_lista)  # ['Ana', 'Luis', 'Sofía', 'David']

# Repetición de listas
repetida = numeros * 2
print(repetida)  # [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]

# Comprobación de existencia de un elemento
print("Ana" in nombres)  # True
print("Carlos" in nombres)  # False

# ========================================
# Resumen
# ========================================

"""
📌 **Resumen sobre Listas en Python**:
- Se crean usando `[]` y pueden contener diferentes tipos de datos.
- Se acceden mediante índices positivos y negativos.
- Se pueden modificar usando métodos como `.append()`, `.remove()`, `.sort()`, `.reverse()`, y `.index()`.
- Se pueden concatenar y repetir.
- Se puede verificar si un elemento existe en la lista con `in`.

✔ Las listas son una de las estructuras más usadas en Python por su flexibilidad y facilidad de manipulación.
"""

# ========================================
# Fin del Documento
# ========================================