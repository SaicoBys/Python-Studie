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
    message = "dentro de la función"  # Se asigna un mensaje a la variable
    print(f"Este mensaje está {message}.")  # Se imprime el mensaje

# Invocación de la función:
sample_function()  # Llama a la función para ejecutar su contenido
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
    if n > 0:  # Verifica si el número es mayor que cero
        print(f"{n} es un número positivo.")  # Imprime que es positivo
    elif n < 0:  # Verifica si el número es menor que cero
        print(f"{n} es un número negativo.")  # Imprime que es negativo
    else:  # Si no es ni mayor ni menor que cero, debe ser cero
        print(f"{n} es cero.")  # Imprime que es cero

# Prueba de la función:
verificar_numero(5)  # Llama a la función con 5
verificar_numero(-3) # Llama a la función con -3
verificar_numero(0)  # Llama a la función con 0

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
    for i in range(1, 6):  # Itera desde 1 hasta 5
        print(i)  # Imprime el número actual

# Invocación de la función:
count_to_five()  # Llama a la función para contar hasta cinco
# Salida:
# 1
# 2
# 3
# 4
# 5

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica sobre indentación

1️⃣ Crea una función llamada `saludo` que imprima "Hola Mundo".

2️⃣ Dentro de un bucle `for`, imprime los números del 1 al 5 usando indentación adecuada.

3️⃣ Crea una función que reciba un número y devuelva si es par o impar, usando estructuras condicionales correctamente indentadas.

4️⃣ Intenta escribir una función con mala indentación y ejecuta el código para ver qué error aparece.
"""

# Espacio para practicar:

# ========================================
# Fin del Documento
# ========================================