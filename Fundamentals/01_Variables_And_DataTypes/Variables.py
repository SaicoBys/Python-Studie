# ========================================
# Variables en Python
# ========================================

"""
## 📌 Descripción
Las **variables** en Python son contenedores que almacenan datos.  
No necesitan declaración previa ni especificar el tipo de dato.

📌 **Características principales de las variables en Python:**
- Se crean al asignarles un valor (`=`).
- Pueden cambiar de tipo en tiempo de ejecución (tipado dinámico).
- No requieren una declaración explícita como en otros lenguajes (`int`, `string`, etc.).
- Sensibles a mayúsculas y minúsculas (`edad` ≠ `Edad`).
"""

# ========================================
# Declaración y asignación de variables
# ========================================

# Asignación de diferentes tipos de datos a variables
nombre = "Alice"  # Variable tipo string (cadena de texto)
edad = 25         # Variable tipo int (entero)
altura = 1.75     # Variable tipo float (decimal)
es_estudiante = True  # Variable tipo bool (booleano)

# Imprimir valores
print(nombre)  # Salida: Alice
print(edad)    # Salida: 25
print(altura)  # Salida: 1.75
print(es_estudiante)  # Salida: True

# ========================================
# Tipado dinámico en Python
# ========================================

"""
Python permite cambiar el tipo de dato de una variable durante la ejecución.
"""

dato = 10        # `dato` es un entero
print(dato)      # Salida: 10

dato = "Hola"    # Ahora `dato` es un string (cambia de int a string)
print(dato)      # Salida: Hola

dato = 3.14      # Ahora `dato` es un float (cambia de string a float)
print(dato)      # Salida: 3.14

# ========================================
# Reasignación de variables
# ========================================

"""
Podemos reasignar el valor de una variable en cualquier momento.
"""

mi_variable = "Python"
print(mi_variable)  # Salida: Python

mi_variable = 2024
print(mi_variable)  # Salida: 2024

# ========================================
# Nombrado de variables y convenciones
# ========================================

"""
Reglas para nombrar variables en Python:
✅ Puede contener letras, números y guiones bajos (`_`).
✅ No puede comenzar con un número (`3variable` ❌).
✅ No puede contener espacios (`mi variable` ❌ → `mi_variable` ✅).
✅ No puede ser una palabra reservada (`def`, `class`, `if`, etc.).
"""

# Nombres válidos
mi_variable = "Hola"
_variable = 42
nombre_completo = "John Doe"

# Nombres inválidos (descomentar para ver errores)
# 3variable = "Error"   ❌ No puede empezar con número
# mi variable = 10       ❌ No puede contener espacios
# def = "Error"          ❌ No puede ser una palabra reservada

# ========================================
# Uso de variables en expresiones
# ========================================

"""
Las variables pueden usarse en operaciones matemáticas y concatenaciones de strings.
"""

# Operaciones matemáticas
a = 10  # tipo int
b = 5   # tipo int
suma = a + b  # int + int
multiplicacion = a * b  # int * int

print(suma)          # Salida: 15
print(multiplicacion)  # Salida: 50

# Concatenación de strings
saludo = "Hola, " + nombre  # string + string
print(saludo)  # Salida: Hola, Alice

# ========================================
# Resumen
# ========================================

"""
## 📌 Resumen
- En Python, las variables se crean asignando un valor con `=`.
- No necesitan declaración previa ni especificar tipo.
- Pueden cambiar de tipo durante la ejecución (tipado dinámico).
- Se pueden usar en operaciones matemáticas y concatenaciones de texto.
- Deben seguir ciertas reglas de nombrado para ser válidas.
"""

# ========================================
# Fin del Documento
# ========================================