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
Creamos varias listas usando corchetes `[]`, incluyendo una lista de números, una de cadenas, una mixta y una vacía.
"""

# Lista de números enteros
numeros = [1, 2, 3, 4, 5]                  
# Lista de cadenas de texto
nombres = ["Ana", "Carlos", "Luis"]       
# Lista con tipos mixtos
mixta = [1, "Python", 3.14, True]         
# Lista vacía
vacia = []                                

print(numeros)   # Muestra la lista de números
print(nombres)   # Muestra la lista de nombres
print(mixta)     # Muestra la lista mixta
print(vacia)     # Muestra la lista vacía

# ========================================
# 2. Acceso a Elementos
# ========================================

"""
Accedemos a elementos por su índice (positivo o negativo) y modificamos uno de ellos.
"""

print(nombres[0])   # Accede al primer elemento: "Ana"
print(nombres[-1])  # Accede al último elemento: "Luis"

nombres[1] = "Pedro"  # Cambia "Carlos" por "Pedro"
print(nombres)        # Muestra la lista modificada

# ========================================
# 3. Métodos Comunes de Listas
# ========================================

"""
Usamos varios métodos comunes de listas para modificar su contenido.
"""

# `.append()` → Agrega un elemento al final
nombres.append("Marta")  
print(nombres)  # Muestra la lista después de agregar "Marta"

# `.remove()` → Elimina la primera ocurrencia de un valor
nombres.remove("Pedro")  
print(nombres)  # Muestra la lista después de eliminar "Pedro"

# `.pop()` → Elimina y devuelve el último elemento (o uno específico)
ultimo = nombres.pop()  
print(ultimo)  # Muestra el último elemento eliminado: 'Marta'
print(nombres)  # Muestra la lista después de eliminar el último elemento

# `.sort()` → Ordena la lista (solo funciona con datos del mismo tipo)
numeros.sort()  
print(numeros)  # Muestra la lista de números ordenada

# `.reverse()` → Invierte el orden de la lista
numeros.reverse()  
print(numeros)  # Muestra la lista de números invertida

# `.index()` → Devuelve la posición de un elemento
print(nombres.index("Ana"))  # Muestra la posición de "Ana" en la lista

# ========================================
# 4. Operaciones con Listas
# ========================================

"""
Realizamos operaciones con listas: concatenación, repetición y verificación de existencia.
"""

# Concatenación de listas
nueva_lista = nombres + ["Sofía", "David"]  
print(nueva_lista)  # Muestra la lista nueva después de la concatenación

# Repetición de listas
repetida = numeros * 2  
print(repetida)  # Muestra la lista de números repetida

# Comprobación de existencia de un elemento
print("Ana" in nombres)  # Verifica si "Ana" está en la lista: True
print("Carlos" in nombres)  # Verifica si "Carlos" está en la lista: False

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
"""
## 🧠 Ejercicios de Práctica
Pon en práctica lo aprendido sobre listas en Python.
"""
# ========================================

# --------------------------------------------------
# 1️⃣ Crear una lista de frutas
# --------------------------------------------------
"""
Crea una lista llamada `frutas` que contenga al menos 4 frutas.
Imprime la lista completa.
"""

# Tu código aquí...


# --------------------------------------------------
# 2️⃣ Acceder y modificar un elemento
# --------------------------------------------------
"""
Accede al segundo elemento de la lista `frutas` y cámbialo por otra fruta.
Imprime la lista resultante.
"""

# Tu código aquí...


# --------------------------------------------------
# 3️⃣ Agregar y eliminar elementos
# --------------------------------------------------
"""
Agrega una nueva fruta a la lista con `.append()`.
Luego elimina una fruta existente usando `.remove()`.
Imprime la lista final.
"""

# Tu código aquí...


# ✅ ¡Sigue practicando para dominar las listas!
# ========================================