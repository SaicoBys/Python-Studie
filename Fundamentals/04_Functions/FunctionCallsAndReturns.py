# ========================================
# Funciones en Python - Llamadas y Retornos
# ========================================

"""
## 📌 Descripción
Las funciones en Python permiten modularizar el código y reutilizarlo de manera eficiente.

📌 **Conceptos clave:**
- **Llamar a una función:** Se hace usando su nombre seguido de paréntesis `()`.
- **`return`:** Permite que la función devuelva valores que pueden ser usados posteriormente.
- **Diferencia entre `print()` y `return`**:
  - `print()` muestra un valor en pantalla, pero no lo devuelve.
  - `return` devuelve un valor que puede ser almacenado o manipulado.
"""

# ========================================
# 1. Llamar a Funciones
# ========================================

"""
Para ejecutar una función en Python, se utiliza su nombre seguido de `()`.
Si la función acepta parámetros, estos deben pasarse dentro de los paréntesis.
"""

# Ejemplo:
def greet():
    """
    Función simple que imprime un saludo.
    """
    print("Hola a todos!")

# Invocación de la función:
greet()
# Salida: Hola a todos!

# ========================================
# 2. Diferencia entre print() y return
# ========================================

"""
📌 `print()` solo muestra información en pantalla.
📌 `return` devuelve un valor que puede ser almacenado y usado posteriormente.
"""

def con_print():
    print("Este valor solo se muestra en pantalla.")

def con_return():
    return "Este valor puede ser almacenado."

resultado = con_return()
print(resultado)  # Salida: Este valor puede ser almacenado.

con_print()  # Salida: Este valor solo se muestra en pantalla.

# ========================================
# 3. Retornar Valores con return
# ========================================

"""
Las funciones pueden retornar valores utilizando `return`. Esto permite capturar y utilizar los resultados.
"""

# Retorno de un solo valor
def sumar(a, b):
    """
    Función que suma dos números y retorna el resultado.
    """
    return a + b

# Uso del valor retornado:
resultado = sumar(5, 3)
print(f"El resultado es {resultado}")
# Salida: El resultado es 8

# ========================================
# 4. Uso de return en if-else
# ========================================

"""
Podemos utilizar `return` dentro de estructuras condicionales para retornar diferentes valores.
"""

def evaluar_nota(nota):
    """
    Retorna si la nota es aprobatoria o reprobatoria.
    """
    if nota >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

estado = evaluar_nota(85)
print(f"Estado del estudiante: {estado}")  # Salida: Estado del estudiante: Aprobado

# ========================================
# 5. Retornar Múltiples Valores
# ========================================

"""
Python permite retornar múltiples valores, que se empaquetan automáticamente en una tupla.
"""

# Ejemplo:
def calcular_operaciones(a, b):
    """
    Función que realiza varias operaciones con dos números y retorna los resultados.
    """
    suma = a + b
    resta = a - b
    return suma, resta

# Desempaquetando los valores retornados:
resultado_suma, resultado_resta = calcular_operaciones(10, 5)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")
# Salida: Suma: 15, Resta: 5

# ========================================
# 6. Uso de return con valores por defecto
# ========================================

"""
Podemos asignar valores por defecto a los parámetros de una función.
Si no se proporciona un valor al llamar la función, se usará el valor por defecto.
"""

def calcular_precio(precio, descuento=0):
    """
    Calcula el precio final aplicando un descuento opcional.
    """
    return precio - (precio * descuento / 100)

precio_final = calcular_precio(100, 10)  # Aplicando 10% de descuento
precio_sin_descuento = calcular_precio(100)  # Sin descuento

print(f"Precio con descuento: {precio_final}")  # Salida: Precio con descuento: 90.0
print(f"Precio sin descuento: {precio_sin_descuento}")  # Salida: Precio sin descuento: 100.0

# ========================================
# Resumen
# ========================================

"""
📌 **Resumen de Llamadas y Retornos en Funciones**:
- Las funciones se llaman con `nombre_funcion()`.
- `return` devuelve valores que pueden ser almacenados o usados posteriormente.
- `print()` solo muestra información en pantalla, pero no devuelve valores.
- Se pueden retornar múltiples valores, que son empaquetados en una tupla.
- Las funciones pueden tener parámetros con valores por defecto.
"""

# ========================================
# Fin del Documento
# ========================================