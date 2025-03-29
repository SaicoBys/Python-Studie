# ========================================
"""
📌 TEMA: Ordenamiento de Listas en Python

Python ofrece métodos incorporados para ordenar listas, ya sea directamente o generando una nueva lista ordenada.

✅ Características:
- `.sort()` ordena la lista en su lugar (modifica la original).
- `.sort(reverse=True)` ordena en orden descendente.
- `sorted(lista)` crea una nueva lista ordenada sin modificar la original.
"""
# ========================================


# --------------------------------------------------
# 🎯 Ejemplo 1: Ordenar lista ascendente con .sort()
# --------------------------------------------------
"""
Ordenamos una lista de nombres en orden alfabético (ascendente) con `.sort()`.
"""

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]  # Lista original
print("Lista original:", names)                          # Mostramos la original

names.sort()                                             # Ordenamos en orden ascendente
print("Lista ordenada:", names)                          # Mostramos la lista ordenada


# --------------------------------------------------
# 🎯 Ejemplo 2: Ordenar lista descendente con .sort(reverse=True)
# --------------------------------------------------
"""
Reordenamos la lista en orden descendente con `.sort(reverse=True)`.
"""

names.sort(reverse=True)                                # Ordenamos en orden descendente
print("Lista ordenada en orden descendente:", names)     # Mostramos la lista ordenada


# --------------------------------------------------
# 🎯 Ejemplo 3: Usar sorted() para nueva lista ordenada
# --------------------------------------------------
"""
Usamos `sorted()` para crear una nueva lista ordenada sin modificar la original.
"""

sorted_names = sorted(names)                             # Creamos una nueva lista ordenada
print("Nueva lista ordenada:", sorted_names)             # Mostramos la nueva lista
print("Lista original sin cambios:", names)              # Verificamos que la original no cambió


# ========================================
"""
📌 RESUMEN

- `.sort()` → Ordena la lista en su lugar.
- `.sort(reverse=True)` → Ordena en orden descendente.
- `sorted(lista)` → Retorna una nueva lista ordenada.
"""
# ========================================


# ========================================
"""
## 🧠 Ejercicios de Práctica
Practica lo aprendido sobre ordenamiento de listas.
"""
# ========================================

# --------------------------------------------------
# 1️⃣ Ordenar Números
# --------------------------------------------------
"""
Crea una lista de números y ordénala de forma ascendente y luego descendente.
Imprime ambas listas.
"""

# Tu código aquí...


# --------------------------------------------------
# 2️⃣ Usar sorted() sin modificar la original
# --------------------------------------------------
"""
Crea una lista de frutas.
Crea una nueva lista ordenada usando `sorted()` sin modificar la original.
Imprime ambas listas para comparar.
"""

# Tu código aquí...


# ========================================
