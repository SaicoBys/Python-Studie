# ========================================
# Introducción a los Bucles en Python
# ========================================

# Descripción:
"""
Este documento sirve como una introducción a los diferentes tipos de bucles en Python,
incluyendo bucles 'for', 'while', y las palabras clave 'break' y 'continue'.
"""

# Bucle 'for':
"""
Un bucle 'for' en Python se utiliza para iterar sobre una secuencia (que puede ser una lista,
una tupla, un diccionario, un conjunto, o una cadena).

Ejemplo básico de un bucle 'for':
"""
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# Palabra clave 'break':
"""
Se utiliza para salir de un bucle cuando se cumple una condición externa.
Ejemplo:
"""
numbers = [0, 254, 2, -1, 3]
for num in numbers:
    if num < 0:
        print("Número negativo detectado, saliendo del bucle.")
        break
    print(num)

# Palabra clave 'continue':
"""
Se utiliza para omitir la parte restante de un bucle.
Ejemplo:
"""
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
    if i < 0:
        continue
    print(i)

# ========================================
# Fin del Documento
# ========================================