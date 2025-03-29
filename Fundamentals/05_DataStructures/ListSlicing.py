# ========================================
"""
📌 TEMA: Rebanado de Listas (Slicing) en Python

El slicing permite extraer sublistas usando la notación `lista[inicio:fin]`.

✅ Características:
- Extrae elementos desde `inicio` hasta `fin - 1`.
- Usa índices positivos y negativos.
- Puede omitirse `inicio` o `fin` para incluir desde el inicio o hasta el final.
"""
# ========================================


# --------------------------------------------------
# 🎯 Ejemplo 1: Extraer una sublista por rango
# --------------------------------------------------
"""
Extraemos una sublista desde el índice 1 hasta el 5 (no incluye el índice 6).
"""

letters = ["a", "b", "c", "d", "e", "f", "g"]  # Lista original
print("Lista original:", letters)

sliced_list = letters[1:6]                     # Extraemos de 'b' a 'f'
print("Sublista desde 'b' hasta 'f':", sliced_list)


# --------------------------------------------------
# 🎯 Ejemplo 2: Últimos tres elementos con índice negativo
# --------------------------------------------------
"""
Extraemos los últimos tres elementos usando índices negativos.
"""

print("Últimos tres elementos:", letters[-3:])  # ['e', 'f', 'g']


# --------------------------------------------------
# 🎯 Ejemplo 3: Omitir los dos últimos elementos
# --------------------------------------------------
"""
Extraemos todos los elementos excepto los dos últimos.
"""

print("Todos excepto los dos últimos:", letters[:-2])  # ['a', 'b', 'c', 'd', 'e']


# ========================================
"""
📌 RESUMEN

- `lista[inicio:fin]` → Extrae desde `inicio` hasta `fin - 1`.
- `lista[:fin]` → Desde el inicio hasta `fin - 1`.
- `lista[inicio:]` → Desde `inicio` hasta el final.
- `lista[-n:]` o `lista[:-n]` → Desde/hasta posiciones relativas al final.
"""
# ========================================


# ========================================
"""
## 🧠 Ejercicios de Práctica
Practica lo aprendido sobre slicing de listas.
"""
# ========================================

# --------------------------------------------------
# 1️⃣ Extraer del segundo al quinto elemento
# --------------------------------------------------
"""
Crea una lista con 8 letras y extrae una sublista desde el segundo hasta el quinto elemento.
"""

# Tu código aquí...


# --------------------------------------------------
# 2️⃣ Obtener los tres últimos elementos
# --------------------------------------------------
"""
De la lista anterior, imprime los últimos tres elementos usando slicing.
"""

# Tu código aquí...


# --------------------------------------------------
# 3️⃣ Omitir los dos primeros y dos últimos
# --------------------------------------------------
"""
Imprime todos los elementos de la lista excepto los dos primeros y los dos últimos.
"""

# Tu código aquí...


# ========================================
