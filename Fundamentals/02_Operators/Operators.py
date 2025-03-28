# ========================================
# Operadores en Python
# ========================================

"""
## Descripción
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
x, y = 10, 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.3333
print(x // y)  # 3
print(x % y)  # 1
print(x ** y)  # 1000 (10^3)

# ========================================
# 2. Operadores de Comparación
# ========================================

"""
Usados para comparar valores:
- `==` (igual a)
- `!=` (diferente de)
- `>` (mayor que)
- `<` (menor que)
- `>=` (mayor o igual que)
- `<=` (menor o igual que)
"""

# Ejemplos
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False

# ========================================
# 3. Operadores Lógicos
# ========================================

"""
Permiten combinar expresiones booleanas:
- `and` (Verdadero si ambas condiciones son verdaderas)
- `or` (Verdadero si al menos una condición es verdadera)
- `not` (Invierte el resultado lógico)
"""

# Ejemplos
cond1, cond2 = True, False
print(cond1 and cond2)  # False
print(cond1 or cond2)   # True
print(not cond1)        # False

# Más ejemplos con `and`, `or`, `not`
edad = 20
es_estudiante = True
print(edad > 18 and es_estudiante)  # True
print(edad < 18 or es_estudiante)   # True
print(not es_estudiante)            # False

# ========================================
# 4. Operadores de Asignación
# ========================================

"""
Usados para asignar valores a variables:
- `=` (asignación)
- `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` (operaciones combinadas)
"""

# Ejemplos
z = 5
z += 3  # Equivalente a z = z + 3
print(z)  # 8
z *= 2  # Equivalente a z = z * 2
print(z)  # 16

# ========================================
# 5. Operadores de Identidad y Pertenencia
# ========================================

"""
- **Operadores de Identidad (`is`, `is not`)**: Comparan si dos objetos son el mismo en memoria.
- **Operadores de Pertenencia (`in`, `not in`)**: Verifican si un elemento está dentro de una colección.
"""

# Ejemplo de Identidad
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
print(lista1 is lista2)  # True (Mismo objeto en memoria)
print(lista1 is lista3)  # False (Distinto objeto con mismos valores)

# Ejemplo de Pertenencia
frutas = ["manzana", "banana", "cereza"]
print("manzana" in frutas)  # True
print("pera" not in frutas)  # True

# ========================================
# Resumen
# ========================================

"""
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
