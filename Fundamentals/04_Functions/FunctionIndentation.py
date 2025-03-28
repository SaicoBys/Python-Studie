# ========================================
# Funciones en Python - Indentación
# ========================================

"""
## 📌 Descripción
La indentación en Python es **obligatoria** y define la estructura del código.
A diferencia de otros lenguajes que usan llaves `{}` o `begin-end`, en Python la indentación determina los bloques de código.

📌 **Importancia de la indentación**:
- **Define la estructura del código**: Python usa espacios en blanco en lugar de llaves `{}`.
- **Evita errores de sintaxis**: La indentación incorrecta provoca `IndentationError`.
- **Mejora la legibilidad**: Un código bien indentado es más fácil de entender y mantener.
"""

# ========================================
# 1. Ejemplo de Indentación Correcta
# ========================================

def sample_function():
    """
    Función que demuestra la importancia de la indentación correcta.
    """
    message = "dentro de la función"
    print(f"Este mensaje está {message}.")

# Invocación de la función:
sample_function()
# Salida: Este mensaje está dentro de la función.

# ========================================
# 2. Consecuencias de Indentación Incorrecta
# ========================================

"""
Una indentación incorrecta puede generar errores de sintaxis.
"""

# ❌ Ejemplo de Error de Indentación (provocará un `IndentationError` si se ejecuta)
def broken_function():
    print("Este código está mal indentado")  # No tiene indentación

# ========================================
# 3. Indentación en Estructuras de Control
# ========================================

"""
La indentación también define el alcance de estructuras de control (`if`, `for`, `while`).
"""

# Ejemplo con estructura if-else:
def verificar_numero(n):
    """
    Función que verifica si un número es positivo, negativo o cero.
    """
    if n > 0:
        print(f"{n} es un número positivo.")
    elif n < 0:
        print(f"{n} es un número negativo.")
    else:
        print(f"{n} es cero.")

# Prueba de la función:
verificar_numero(5)  # Salida: 5 es un número positivo.
verificar_numero(-3) # Salida: -3 es un número negativo.
verificar_numero(0)  # Salida: 0 es cero.

# ========================================
# 4. Indentación en Bucles
# ========================================

"""
Los bucles en Python requieren indentación para definir su contenido.
"""

# Ejemplo con un bucle for:
def count_to_five():
    """
    Función que cuenta hasta cinco, demostrando la indentación en un bucle.
    """
    for i in range(1, 6):
        print(i)

# Invocación de la función:
count_to_five()
# Salida:
# 1
# 2
# 3
# 4
# 5

# ========================================
# Resumen
# ========================================

"""
📌 **Resumen de la Indentación en Python**:
- La indentación es obligatoria en Python.
- Define el alcance de funciones, bucles y estructuras de control.
- La indentación incorrecta genera `IndentationError`.
- Un código bien indentado es más legible y fácil de mantener.
"""

# ========================================
# Fin del Documento
# ========================================