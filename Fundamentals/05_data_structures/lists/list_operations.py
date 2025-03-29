# ========================================
"""
📌 TEMA: Operaciones con Listas en Python

Las listas permiten agregar, eliminar, contar y buscar elementos utilizando métodos integrados.

✅ Características:
- `.append()` agrega un elemento al final.
- `.remove()` elimina la primera ocurrencia de un valor.
- `.count()` cuenta cuántas veces aparece un elemento en la lista.
- Se pueden combinar con estructuras de control para modificar dinámicamente su contenido.
"""
# ========================================


# --------------------------------------------------
# 🎯 Ejemplo: Agregar elementos con .append()
# --------------------------------------------------
"""
Usamos `.append()` para agregar un nuevo elemento al final de la lista.
"""

orders = ['daisies', 'periwinkle']       # Lista inicial de órdenes
orders.append('tulips')                  # Agregamos 'tulips' al final
print("Órdenes actuales:", orders)       # Mostramos la lista actualizada


# --------------------------------------------------
# 🎯 Ejemplo: Eliminar elementos con .remove()
# --------------------------------------------------
"""
Usamos `.remove()` para eliminar la primera ocurrencia del elemento especificado.
"""

orders.remove('daisies')                 # Eliminamos 'daisies' de la lista
print("Después de remover margaritas:", orders)  # Mostramos la lista actualizada


# --------------------------------------------------
# 🎯 Ejemplo: Contar elementos con .count()
# --------------------------------------------------
"""
Usamos `.count()` para contar cuántas veces aparece un valor en la lista.
"""

print("Número de 'tulips' en las órdenes:", orders.count('tulips'))  # Mostramos cuántas veces aparece 'tulips'


# ========================================
"""
📌 RESUMEN

- `.append(x)` → Agrega `x` al final de la lista.
- `.remove(x)` → Elimina la primera ocurrencia de `x`.
- `.count(x)` → Devuelve cuántas veces aparece `x` en la lista.
"""
# ========================================


# ========================================
"""
## 🧠 Ejercicios de Práctica
Practica lo aprendido sobre operaciones con listas.
"""
# ========================================

# --------------------------------------------------
# 1️⃣ Agregar Elementos a una Lista
# --------------------------------------------------
"""
Crea una lista de nombres y agrega tres elementos usando `.append()`.
Muestra la lista resultante.
"""

# Tu código aquí...


# --------------------------------------------------
# 2️⃣ Eliminar un Elemento
# --------------------------------------------------
"""
Crea una lista de frutas. Elimina una fruta específica usando `.remove()`.
Muestra la lista después de la eliminación.
"""

# Tu código aquí...


# --------------------------------------------------
# 3️⃣ Contar Elementos
# --------------------------------------------------
"""
Crea una lista de colores con repeticiones. Usa `.count()` para contar cuántas veces aparece un color específico.
"""

# Tu código aquí...


# ========================================
