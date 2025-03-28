# ========================================
# Tipos de Datos en Python
# ========================================

"""
## Descripción
Python ofrece varios tipos de datos incorporados que permiten al programador realizar diferentes operaciones.
Comprender estos tipos de datos es esencial para manipular correctamente la información dentro de tus programas.

### Tipos de Datos Básicos
- **Enteros (`int`)**: Números sin parte decimal. Usados comúnmente para contar o iterar.
- **Números de punto flotante (`float`)**: Números con parte decimal. Utilizados en cálculos que requieren precisión.
- **Cadenas de texto (`str`)**: Secuencias de caracteres utilizadas para almacenar texto.
- **Booleanos (`bool`)**: Representan valores de verdad (`True` o `False`). Utilizados para controlar el flujo del programa y hacer validaciones.
"""

# ========================================
# Enteros
# ========================================

edad = 30  # Asignación de un entero
cantidad_alumnos = 25  # Otro ejemplo de entero

print(f"Edad: {edad}, Alumnos: {cantidad_alumnos}")

# ========================================
# Números de punto flotante
# ========================================

precio = 19.99  # Asignación de un flotante
pi = 3.14159  # Constante matemática pi
temperatura = -5.6  # Número negativo con decimales

print(f"Precio: {precio}, Pi: {pi}, Temperatura: {temperatura}")

# ========================================
# Cadenas de texto
# ========================================

nombre = "María"  # Una simple cadena de texto
mensaje = '¡Hola, mundo!'  # Otra cadena usando comillas simples

print(f"Nombre: {nombre}, Mensaje: {mensaje}")

# ========================================
# Booleanos
# ========================================

es_mayor_de_edad = True  # Verdadero
tiene_descuento = False  # Falso

if es_mayor_de_edad:
    print("Puede ingresar al evento.")
else:
    print("No puede ingresar al evento.")

# ========================================
# Datos Compuestos
# ========================================

"""
## Datos Compuestos
Además de los tipos básicos, Python permite estructuras de datos más complejas que incluyen:
- **Listas (`list`)**: Colecciones ordenadas y mutables de elementos.
- **Tuplas (`tuple`)**: Colecciones ordenadas e inmutables de elementos.
- **Diccionarios (`dict`)**: Colecciones de pares clave-valor, sin ordenar y mutables.
- **Conjuntos (`set`)**: Colecciones no ordenadas de elementos únicos.
"""

# ========================================
# Listas
# ========================================

frutas = ["manzana", "banana", "cereza"]  # Lista de frutas
frutas.append("naranja")  # Agregar elemento a la lista
print(f"Lista de frutas: {frutas}")

# ========================================
# Tuplas
# ========================================

dimensiones = (20, 50, 30)  # Dimensiones como tupla
print(f"Dimensiones: {dimensiones}")

# ========================================
# Diccionarios
# ========================================

usuario = {
    "nombre": "Juan",
    "edad": 28,
    "email": "juan@example.com"
}  # Diccionario con información de usuario

print(f"Nombre del usuario: {usuario['nombre']}, Email: {usuario['email']}")

# ========================================
# Conjuntos
# ========================================

colores = {"rojo", "verde", "azul"}  # Conjunto de colores
colores.add("amarillo")  # Agregar un elemento único
print(f"Colores disponibles: {colores}")

# ========================================
# Conversión de Tipos (Type Casting)
# ========================================

"""
## Conversión de Tipos
Python permite convertir entre tipos de datos mediante funciones integradas:
- `int()`: Convierte a entero.
- `float()`: Convierte a flotante.
- `str()`: Convierte a cadena de texto.
- `bool()`: Convierte a booleano.
"""

numero_texto = "100"
numero_convertido = int(numero_texto)  # Convierte string a entero
print(f"Número convertido: {numero_convertido}, Tipo: {type(numero_convertido)}")

# ========================================
# Resumen
# ========================================

"""
## Resumen
Cada tipo de dato en Python tiene su propósito y uso específico según las necesidades del programa.
Aprender a elegir el tipo de dato adecuado es clave para desarrollar soluciones eficientes y claras.

### Consideraciones
- La elección del tipo de datos afecta directamente a la memoria y la eficiencia del programa.
- Python es dinámicamente tipado, lo que significa que no necesitas declarar el tipo de una variable al momento de su creación.
- Se pueden realizar conversiones de tipos (`int()`, `float()`, `str()`, etc.) cuando sea necesario.
"""

# ========================================
# Fin del Documento
# ========================================