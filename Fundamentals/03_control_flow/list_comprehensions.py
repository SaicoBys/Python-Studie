# ========================================
# Comprensiones de Listas en Python
# ========================================

# Descripción:
"""
Explora cómo las comprensiones de listas permiten generar listas de manera concisa y eficiente. Aprenderás a incluir condiciones y manejar múltiples escenarios dentro de una sola línea de código.

🔹 Sintaxis básica:
[expresión for elemento in iterable]

- expresión → lo que quieres hacer con cada elemento.
- for elemento in iterable → recorre cada valor en la secuencia original.

🔹 Sintaxis con condicional (filtro):
[expresión for elemento in iterable if condición]

- Solo incluye los elementos que cumplan la condición.

🔹 Sintaxis con if-else (condicional ternario):
[expresión1 if condición else expresión2 for elemento in iterable]

- Aplica una transformación distinta según una condición.
"""

# Comprensión Básica:
"""
Crea una lista cuyos elementos son el doble de los valores de otra lista.
"""
# Ejemplo:
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)
# Salida: [2, 4, 6, 8, 10]

# Comprensión con Condicional 'if':
"""
Genera una lista solo con los números negativos duplicados de la lista original.
"""
# Ejemplo:
mixed_numbers = [10, -20, 30, -40, 50]
doubled_negatives = [x * 2 for x in mixed_numbers if x < 0]
print(doubled_negatives)
# Salida: [-40, -80]

# Comprensión con Condicional 'if-else':
"""
Duplica los negativos y triplica los positivos en la lista.
"""
# Ejemplo:
adjusted_numbers = [x * 2 if x < 0 else x * 3 for x in mixed_numbers]
print(adjusted_numbers)
# Salida: [30, -40, 90, -80, 150]

# ========================================
# Resumen
# ========================================

"""
## 📌 Resumen
- Las comprensiones de listas permiten crear listas de forma concisa.
- Se componen de una expresión, un bucle `for`, y opcionalmente condiciones `if` o expresiones ternarias (`if-else`).
- Son más legibles y eficientes que los bucles tradicionales en muchos casos.
- Puedes aplicar filtros con `if` o lógica condicional con `if-else` directamente dentro de la comprensión.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica para List Comprehensions

1️⃣ Genera una lista con los cuadrados de los números del 1 al 10.

2️⃣ Crea una lista con los números pares del 1 al 20.

3️⃣ Dada una lista de nombres, genera una nueva lista con solo los nombres que comienzan con la letra "A".

4️⃣ A partir de una lista de edades, genera una lista con "Mayor" si la edad es mayor o igual a 18, o "Menor" si es menor.

5️⃣ (🔒 Este ejercicio requiere diccionarios) Filtra una lista de usuarios para obtener solo los nombres de aquellos que están activos.
"""

# --------------------------------------------------
# 1️⃣ Genera una lista con los cuadrados de los números del 1 al 10
# --------------------------------------------------

result = [x ** 2 for x in range(1, 11)]
print(result)

# --------------------------------------------------
# 2️⃣ Crea una lista con los números pares del 1 al 20
# --------------------------------------------------

pairs_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(pairs_numbers)

# --------------------------------------------------
# 3️⃣ Nombres que comienzan con "A"
# --------------------------------------------------


# --------------------------------------------------
# 4️⃣ Clasificación de edades: "Mayor" o "Menor"
# --------------------------------------------------


# --------------------------------------------------
# 5️⃣ Usuarios activos (requiere diccionarios)
# --------------------------------------------------

# 🔒 Este ejercicio se resolverá más adelante cuando veas diccionarios.

# ========================================
# Fin del Documento
# ========================================