# ========================================
# Operadores en Python
# ========================================

"""
## 📌 Descripción
Los operadores en Python son símbolos que realizan operaciones sobre valores y variables.
Se pueden clasificar en diferentes categorías:

1. **Operadores Aritméticos**: Realizan operaciones matemáticas básicas.
2. **Operadores de Comparación**: Comparan dos valores y devuelven un booleano.
3. **Operadores Lógicos**: Permiten combinar expresiones condicionales.
4. **Operadores de Asignación**: Se usan para asignar valores a variables.
5. **Operadores de Identidad y Pertenencia**: Comparan objetos y verifican membresía en colecciones.
"""

# ========================================
# 1. Operadores Aritméticos
# ========================================

"""
## 📌 Descripción
Operadores básicos:
- `+` (suma)
- `-` (resta)
- `*` (multiplicación)
- `/` (división, devuelve flotante)
- `//` (división entera)
- `%` (módulo, residuo de la división)
- `**` (potencia)
"""

# Ejemplos
x, y = 10, 3  # Asignación de valores a x e y
print(x + y)  # 13: Suma de x e y
print(x - y)  # 7: Resta de x e y
print(x * y)  # 30: Multiplicación de x e y
print(x / y)  # 3.3333: División de x entre y, resultado flotante
print(x // y)  # 3: División entera de x entre y
print(x % y)  # 1: Módulo de x entre y, residuo de la división
print(x ** y)  # 1000: Potencia de x elevado a y (10^3)

# ========================================
# 2. Operadores de Comparación
# ========================================

"""
## 📌 Descripción
Usados para comparar valores:
- `==` (igual a)
- `!=` (diferente de)
- `>` (mayor que)
- `<` (menor que)
- `>=` (mayor o igual que)
- `<=` (menor o igual que)
"""

# Ejemplos
print(x == y)  # False: Verifica si x es igual a y
print(x != y)  # True: Verifica si x es diferente de y
print(x > y)   # True: Verifica si x es mayor que y
print(x < y)   # False: Verifica si x es menor que y
print(x >= y)  # True: Verifica si x es mayor o igual que y
print(x <= y)  # False: Verifica si x es menor o igual que y

# ========================================
# 3. Operadores Lógicos
# ========================================

"""
## 📌 Descripción
Permiten combinar expresiones booleanas:
- `and` (Verdadero si ambas condiciones son verdaderas)
- `or` (Verdadero si al menos una condición es verdadera)
- `not` (Invierte el resultado lógico)
"""

# Ejemplos
cond1, cond2 = True, False  # Asignación de valores a cond1 y cond2
print(cond1 and cond2)  # False: Ambas condiciones deben ser verdaderas
print(cond1 or cond2)   # True: Al menos una condición es verdadera
print(not cond1)        # False: Invierte el resultado de cond1

# Más ejemplos con `and`, `or`, `not`
edad = 20  # Asignación de valor a edad
es_estudiante = True  # Asignación de estado de estudiante
print(edad > 18 and es_estudiante)  # True: Verifica condiciones
print(edad < 18 or es_estudiante)   # True: Verifica condiciones
print(not es_estudiante)            # False: Invierte el estado de es_estudiante

# ========================================
# 4. Operadores de Asignación
# ========================================

"""
## 📌 Descripción
Usados para asignar valores a variables:
- `=` (asignación)
- `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` (operaciones combinadas)
"""

# Ejemplos
z = 5  # Asignación de valor inicial a z
z += 3  # Equivalente a z = z + 3
print(z)  # 8: Imprime el nuevo valor de z
z *= 2  # Equivalente a z = z * 2
print(z)  # 16: Imprime el nuevo valor de z

# ========================================
# 5. Operadores de Identidad y Pertenencia
# ========================================

"""
## 📌 Descripción
- **Operadores de Identidad (`is`, `is not`)**: Comparan si dos objetos son el mismo en memoria.
- **Operadores de Pertenencia (`in`, `not in`)**: Verifican si un elemento está dentro de una colección.
"""

# Ejemplo de Identidad
lista1 = [1, 2, 3]  # Asignación de lista a lista1
lista2 = lista1  # lista2 referencia a lista1
lista3 = [1, 2, 3]  # Asignación de nueva lista a lista3
print(lista1 is lista2)  # True: Mismo objeto en memoria
print(lista1 is lista3)  # False: Distinto objeto con mismos valores

# Ejemplo de Pertenencia
frutas = ["manzana", "banana", "cereza"]  # Asignación de lista de frutas
print("manzana" in frutas)  # True: Verifica si "manzana" está en frutas
print("pera" not in frutas)  # True: Verifica si "pera" no está en frutas

# ========================================
# Resumen
# ========================================
"""
## 📌 Resumen
- **Aritméticos**: Realizan cálculos matemáticos.
- **Comparación**: Comparan valores y devuelven `True` o `False`.
- **Lógicos**: Combinan condiciones booleanas.
- **Asignación**: Asignan valores a variables.
- **Identidad**: Comparan objetos en memoria.
- **Pertenencia**: Verifican si un elemento está en una colección.

Comprender estos operadores es crucial para escribir código eficiente y estructurado.
"""

# ========================================
# Fin del Documento
# ========================================
