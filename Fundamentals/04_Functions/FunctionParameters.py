# ========================================
# Funciones en Python - Parámetros y Argumentos
# ========================================

"""
## Descripción
Las funciones utilizan **parámetros** para recibir datos como argumentos, permitiendo que sean flexibles y adaptables a diferentes situaciones.

### Diferencia entre Parámetros y Argumentos
- **Parámetros**: Variables definidas en la declaración de la función.
- **Argumentos**: Valores que se pasan a la función cuando se llama.

Python permite varios tipos de parámetros:
1. **Parámetros Posicionales** (obligatorios en orden específico).
2. **Parámetros con Palabras Clave (`keyword arguments`)**.
3. **Parámetros con Valores por Defecto**.
4. **Argumentos Variables (`*args`, `**kwargs`)**.
"""

# ========================================
# 1. Parámetros Posicionales
# ========================================

"""
Los parámetros posicionales deben proporcionarse en el orden en que están definidos en la función.
"""

def print_name(name):
    """Función que recibe un nombre como parámetro y lo imprime."""
    print(f"Nombre: {name}")

# Invocación de la función:
print_name('Alice')  # Salida: Nombre: Alice

# ========================================
# 2. Múltiples Parámetros
# ========================================

def describe_pet(animal, name):
    """Función que describe un animal proporcionando su tipo y nombre."""
    print(f"Yo tengo un {animal} llamado {name}.")

describe_pet('perro', 'Rex')  # Salida: Yo tengo un perro llamado Rex.

def calcular_area(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2

print(calcular_area(10, 5))  # Salida: 25.0

# ========================================
# 3. Parámetros con Palabras Clave (Keyword Arguments)
# ========================================

"""
En lugar de depender del orden, se pueden especificar los argumentos por su nombre.
Esto mejora la legibilidad y flexibilidad.
"""

def crear_usuario(nombre, edad, ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

crear_usuario(edad=30, nombre="Juan", ciudad="Madrid")  # Orden flexible

# ========================================
# 4. Parámetros con Valores por Defecto
# ========================================

def describe_city(city, country='Italia'):
    """Función que describe una ciudad y su país, con un valor por defecto para el país."""
    print(f"{city} está en {country}.")

describe_city('Roma')  # Usa el valor por defecto

describe_city('Madrid', 'España')  # Sobreescribe el valor por defecto

# ========================================
# 5. Argumentos Variables (*args y **kwargs)
# ========================================

"""
- `*args`: Permite pasar un número variable de argumentos posicionales.
- `**kwargs`: Permite pasar un número variable de argumentos con nombre.
"""

def sumar(*numeros):
    """Suma cualquier cantidad de números."""
    return sum(numeros)

print(sumar(1, 2, 3, 4, 5))  # 15

def mostrar_info(**datos):
    """Muestra información de un usuario con argumentos clave-valor."""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=22, ciudad="Madrid")

# ========================================
# Resumen
# ========================================

"""
- **Parámetros Posicionales**: Se pasan en un orden específico.
- **Keyword Arguments**: Se pueden pasar en cualquier orden especificando el nombre del parámetro.
- **Parámetros con Valores por Defecto**: Si no se proporciona un valor, usa el predeterminado.
- **`*args`** permite recibir múltiples valores posicionales.
- **`**kwargs`** permite recibir múltiples valores clave-valor.

Comprender el uso de parámetros mejora la flexibilidad y reutilización de las funciones en Python.
"""

# ========================================
# Fin del Documento
# ========================================
