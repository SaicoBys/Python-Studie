# ========================================
# Concepto de Variables en Python
# ========================================

"""
## Descripción
Las variables en Python se utilizan para almacenar valores en memoria. No necesitan una declaración de tipo explícita,
ya que Python es un lenguaje de tipado dinámico.

Reglas para definir variables:
- Deben comenzar con una letra o un guion bajo `_`.
- Pueden contener letras, números y guiones bajos.
- No pueden usar palabras reservadas de Python.
- Python es **case-sensitive**, por lo que `edad` y `Edad` son diferentes.
"""

# ========================================
# Declaración y Asignación de Variables
# ========================================

# Ejemplo de variables
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

print(nombre, edad, altura, es_estudiante)

# ========================================
# Reasignación y Tipado Dinámico
# ========================================

"""
Las variables pueden cambiar de tipo en tiempo de ejecución.
"""
valor = 10
print(type(valor))  # <class 'int'>
valor = "Ahora soy un string"
print(type(valor))  # <class 'str'>

# ========================================
# Asignación Múltiple
# ========================================

"""
Se pueden asignar múltiples valores en una sola línea.
"""
a, b, c = 5, 3.2, "Hola"
print(a, b, c)

# ========================================
# Variables Globales y Locales
# ========================================

"""
- Las variables **locales** se definen dentro de una función y no pueden ser accedidas fuera de ella.
- Las variables **globales** se definen fuera de cualquier función y pueden ser accedidas en todo el programa.
"""

def funcion():
    variable_local = "Soy local"
    print(variable_local)

variable_global = "Soy global"

funcion()
print(variable_global)

# ========================================
# Eliminar Variables con del
# ========================================

"""
Se puede eliminar una variable usando `del`.
"""
variable = "Voy a ser eliminada"
del variable
# print(variable)  # Esto generaría un error porque la variable ha sido eliminada.

# ========================================
# Resumen
# ========================================

"""
## Resumen
- Las variables almacenan valores y pueden cambiar de tipo dinámicamente.
- Se pueden asignar múltiples valores en una línea.
- Existen variables locales (dentro de funciones) y globales (fuera de funciones).
- `del` se usa para eliminar variables.
"""

# ========================================
# Fin del Documento
# ========================================
