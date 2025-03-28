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

edad = 30  # Asignación de un número entero a la variable 'edad'
cantidad_alumnos = 25  # Asignación de un número entero a la variable 'cantidad_alumnos'

print(f"Edad: {edad}, Alumnos: {cantidad_alumnos}")  # Imprime los valores usando f-strings

# ========================================
# Números de punto flotante
# ========================================

precio = 19.99  # Asignación de un número decimal a 'precio'
pi = 3.14159  # Asignación de un número decimal a 'pi'
temperatura = -5.6  # Asignación de un número decimal negativo a 'temperatura'

print(f"Precio: {precio}, Pi: {pi}, Temperatura: {temperatura}")  # Imprime los valores

# ========================================
# Cadenas de texto
# ========================================

nombre = "María"  # Cadena de texto con comillas dobles
mensaje = '¡Hola, mundo!'  # Cadena de texto con comillas simples

print(f"Nombre: {nombre}, Mensaje: {mensaje}")  # Imprime nombre y mensaje

# ========================================
# Booleanos
# ========================================

es_mayor_de_edad = True  # Variable booleana con valor True
tiene_descuento = False  # Variable booleana con valor False

if es_mayor_de_edad:  # Condición evaluada como verdadera
    print("Puede ingresar al evento.")  # Se ejecuta si la condición es verdadera
else:
    print("No puede ingresar al evento.")  # Se ejecuta si la condición es falsa

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

frutas = ["manzana", "banana", "cereza"]  # Lista de cadenas de texto
frutas.append("naranja")  # Agrega un nuevo elemento al final de la lista

print(f"Lista de frutas: {frutas}")  # Imprime la lista actualizada

# ========================================
# Tuplas
# ========================================

dimensiones = (20, 50, 30)  # Tupla con tres elementos

print(f"Dimensiones: {dimensiones}")  # Imprime los valores de la tupla

# ========================================
# Diccionarios
# ========================================

usuario = {
    "nombre": "Juan",  # Clave: 'nombre' con valor 'Juan'
    "edad": 28,        # Clave: 'edad' con valor entero
    "email": "juan@example.com"  # Clave: 'email' con valor string
}  # Diccionario con información de usuario

print(f"Nombre del usuario: {usuario['nombre']}, Email: {usuario['email']}")  # Acceso por clave

# ========================================
# Conjuntos
# ========================================

colores = {"rojo", "verde", "azul"}  # Conjunto de colores
colores.add("amarillo")  # Agrega 'amarillo' si no está presente

print(f"Colores disponibles: {colores}")  # Imprime todos los elementos únicos del conjunto

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

numero_texto = "100"  # String con un número
numero_convertido = int(numero_texto)  # Convierte string a entero

print(f"Número convertido: {numero_convertido}, Tipo: {type(numero_convertido)}")  # Muestra el valor convertido y su tipo

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