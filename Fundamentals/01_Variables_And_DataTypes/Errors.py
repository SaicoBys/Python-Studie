# ========================================
# Manejo de Errores en Python
# ========================================

"""
## 📌 Descripción
El manejo de errores es una parte esencial de la programación, ya que permite detectar y responder a situaciones inesperadas que ocurren durante la ejecución del programa.

Python proporciona un mecanismo para capturar errores y evitar que el programa se detenga abruptamente. Estos errores pueden ser:
- **Errores de sintaxis** (`SyntaxError`)
- **Errores en tiempo de ejecución** como `NameError`, `TypeError`, `ZeroDivisionError`, entre otros.
"""

# ========================================
# Ejemplo de SyntaxError
# ========================================

"""
Un `SyntaxError` ocurre cuando escribimos una instrucción que no cumple con las reglas del lenguaje.
"""

try:
    eval('x === x')  # Error de sintaxis: '===' no es un operador válido en Python
except SyntaxError as e:
    print("SyntaxError:", e)

# ========================================
# Ejemplo de NameError
# ========================================

"""
Un `NameError` ocurre cuando intentamos usar una variable que no ha sido definida.
"""

# try:
#     print(variable_inexistente)  # Variable no definida
# except NameError as e:
#     print("NameError:", e)

# ========================================
# Ejemplo de ZeroDivisionError
# ========================================

"""
Un `ZeroDivisionError` ocurre cuando intentamos dividir un número entre cero.
"""

try:
    resultado = 10 / 0  # División entre cero
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# ========================================
# Resumen
# ========================================

"""
## ✅ Resumen

- `SyntaxError`: Se produce cuando el código no cumple con las reglas de sintaxis de Python.
- `NameError`: Se produce cuando se hace referencia a una variable que no ha sido definida.
- `ZeroDivisionError`: Se produce cuando se intenta dividir un número entre cero.
- El uso de `try` y `except` permite capturar y manejar errores para evitar que el programa falle.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica

1️⃣ Crea un bloque `try/except` que capture un `TypeError`.

2️⃣ Intenta convertir un string no numérico a entero con `int("hola")` y maneja el `ValueError`.

3️⃣ Intenta acceder a un índice inválido en una lista y maneja el `IndexError`.

4️⃣ Usa un `try/except` para capturar cualquier error genérico y mostrar el mensaje "Ocurrió un error".

✅ Escribe tus soluciones debajo de cada enunciado:
"""

# --------------------------------------------------
# 1️⃣ TypeError
# --------------------------------------------------


# --------------------------------------------------
# 2️⃣ ValueError
# --------------------------------------------------


# --------------------------------------------------
# 3️⃣ IndexError
# --------------------------------------------------


# --------------------------------------------------
# 4️⃣ Manejo genérico de errores
# --------------------------------------------------


# ========================================
# Fin del Documento
# ========================================