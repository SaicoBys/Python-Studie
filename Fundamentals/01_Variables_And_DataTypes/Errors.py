# errors.py

# ========================================
# Manejo de Errores en Python
# ========================================
"""
## Descripción
El manejo de errores es crucial para desarrollar aplicaciones robustas y fiables. Python ofrece varias maneras de gestionar errores que ocurren durante la ejecución del programa.

## Tipos de Errores Comunes
"""

# SyntaxError
try:
    eval('x === x')  # Código incorrecto que genera SyntaxError
except SyntaxError as e:
    print("SyntaxError:", e)

# NameError
""" try:
    print(inexistent_variable)  # Intento de imprimir una variable no definida
except NameError as e:
    print("NameError:", e) """

# ZeroDivisionError
try:
    result = 10 / 0  # Intento de dividir por cero
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

"""
## Resumen
Entender estos errores comunes y saber cómo manejarlos es esencial para escribir código confiable y fácil de mantener.
"""

# ========================================
# Fin del Documento
# ========================================