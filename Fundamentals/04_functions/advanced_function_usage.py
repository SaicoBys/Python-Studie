# ========================================
# Funciones en Python - Uso Avanzado
# ========================================

"""
## 📌 Descripción
Este documento explora usos avanzados de funciones en Python, que permiten escribir código más flexible, modular y eficiente.

📌 **Conceptos clave:**
- Argumentos por palabra clave (`keyword arguments`).
- Argumentos con valores predeterminados.
- Uso de `*args` y `**kwargs` para manejar múltiples argumentos.
- Funciones anidadas y cierres (closures).
- Decoradores (`@staticmethod`, `@classmethod`, `@property`, `@lru_cache`).
- Funciones de orden superior como `map()`, `filter()`, `zip()`, y `reduce()`.
"""

# ========================================
# 1. Argumentos por Palabra Clave (Keyword Arguments)
# ========================================

"""
Los argumentos por palabra clave permiten que los valores sean pasados a funciones especificando los nombres de los parámetros.
Esto mejora la claridad y flexibilidad del código.
"""

def full_name(first, last):
    """Construye un nombre completo a partir de un nombre y un apellido."""
    return f"{first} {last}"

# Invocación utilizando argumentos por palabra clave:
print(full_name(first='John', last='Doe'))  # Salida: John Doe
print(full_name(last='Doe', first='Jane'))  # Salida: Jane Doe

# ========================================
# 2. Argumentos con Valores Predeterminados
# ========================================

"""
Los valores predeterminados permiten definir parámetros opcionales en una función.
"""

def make_coffee(size='medium', type='black'):
    """Prepara un café con tamaño y tipo especificado."""
    print(f"Making a {size} {type} coffee.")

make_coffee()  # Salida: Making a medium black coffee.
make_coffee('large', 'latte')  # Salida: Making a large latte coffee.

# ========================================
# 3. Uso de *args y **kwargs
# ========================================

"""
📌 `*args` permite pasar múltiples valores posicionales como una tupla.
📌 `**kwargs` permite pasar múltiples pares clave-valor como un diccionario.
"""

def setup_profile(name, email, *interests, **details):
    """Configura un perfil con información adicional."""
    profile = {'name': name, 'email': email, 'interests': interests}
    profile.update(details)
    return profile

# Invocación de la función con información adicional:
profile = setup_profile('John Doe', 'johndoe@example.com', 'coding', 'music', location='USA', age=30)
print(profile)

# ========================================
# 4. Funciones Anidadas y Closures
# ========================================

"""
📌 Un closure es una función que recuerda valores del ámbito externo incluso después de que la función ha terminado.
"""

def generar_multiplicador(factor):
    """Retorna una función que multiplica por el factor dado."""
    def multiplicador(numero):
        return numero * factor
    return multiplicador

multiplicar_por_3 = generar_multiplicador(3)
print(multiplicar_por_3(10))  # Salida: 30

# ========================================
# 5. Decoradores en Python
# ========================================

"""
📌 Los decoradores son funciones que modifican el comportamiento de otras funciones sin cambiar su código.
"""

from functools import lru_cache

@lru_cache(maxsize=10)
def factorial(n):
    """Calcula el factorial de un número utilizando recursión con cache."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120 (se almacena en caché)

# Decoradores en Clases
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @staticmethod
    def saludar():
        return "Hola!"

    @classmethod
    def crear_desde_edad(cls, edad):
        return cls("Desconocido", edad)

    @property
    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años."

persona = Persona("Ana", 30)
print(persona.descripcion)  # Ana tiene 30 años.
print(Persona.saludar())  # Hola!
print(Persona.crear_desde_edad(25).descripcion)  # Desconocido tiene 25 años.

# ========================================
# 6. Funciones de Orden Superior: map(), filter(), zip(), reduce()
# ========================================

"""
📌 `map()` aplica una función a cada elemento de una lista.
📌 `filter()` filtra elementos según una condición.
📌 `zip()` combina múltiples listas en tuplas.
📌 `reduce()` aplica una función acumulativa a una lista.
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5]

# `map()` aplica una función a cada elemento de una lista
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8, 10]

# `filter()` filtra elementos según una condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# `zip()` combina múltiples listas en tuplas
nombres = ['Ana', 'Luis', 'Carlos']
edades = [25, 30, 22]
zipped = list(zip(nombres, edades))
print(zipped)  # [('Ana', 25), ('Luis', 30), ('Carlos', 22)]

# `reduce()` aplica una función acumulativa a una lista
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 15

# ========================================
# Resumen
# ========================================

"""
📌 **Resumen de Funciones Avanzadas en Python**:
- **Keyword Arguments**: Permiten pasar valores especificando nombres de parámetros.
- **Valores Predeterminados**: Permiten definir valores por defecto en los parámetros.
- **`*args` y `**kwargs`**: Permiten manejar múltiples argumentos dinámicos.
- **Closures**: Funciones anidadas que recuerdan el valor de variables externas.
- **Decoradores**: Modifican funciones sin cambiar su código (`@staticmethod`, `@classmethod`, `@lru_cache`).
- **Funciones de Orden Superior**: `map()`, `filter()`, `zip()`, `reduce()` aplican funciones a colecciones de datos.

✔ Estos conceptos avanzados mejoran la eficiencia y flexibilidad del código en Python.
"""

# ========================================
# Ejercicios de Práctica
# ========================================
 
"""
## 🧠 Ejercicios de práctica para Funciones Avanzadas
 
1️⃣ Crea una función `saludo_personalizado` que reciba `nombre` y `mensaje` como argumentos por palabra clave e imprima un saludo.
 
2️⃣ Define una función `crear_usuario` con argumentos predeterminados `nombre='Invitado'` y `activo=True`. Imprímelos.
 
3️⃣ Escribe una función `registrar_datos` que use `*args` para imprimir cualquier cantidad de datos personales.
 
4️⃣ Escribe una función `crear_config` que reciba `**kwargs` con claves como 'theme', 'language', 'timezone' y las imprima.
 
5️⃣ Crea una función `multiplicador_por(factor)` que retorne una función closure que multiplique por ese factor.
 
6️⃣ Usa un decorador para cronometrar cuánto tarda en ejecutarse una función que imprima los primeros 1000 números.
 
7️⃣ Aplica `map()` para elevar al cuadrado una lista de números.
 
8️⃣ Usa `filter()` para extraer solo las palabras de más de 5 letras en una lista de strings.
 
9️⃣ Usa `zip()` para emparejar una lista de nombres con edades y mostrarlo como un diccionario.
 
🔟 Usa `reduce()` para multiplicar todos los elementos de una lista de enteros.
"""
 
# --------------------------------------------------
# 1️⃣ Argumentos por palabra clave
# --------------------------------------------------
 
 
# --------------------------------------------------
# 2️⃣ Argumentos con valores predeterminados
# --------------------------------------------------
 
 
# --------------------------------------------------
# 3️⃣ Uso de *args
# --------------------------------------------------
 
 
# --------------------------------------------------
# 4️⃣ Uso de **kwargs
# --------------------------------------------------
 
 
# --------------------------------------------------
# 5️⃣ Funciones anidadas (closure)
# --------------------------------------------------
 
 
# --------------------------------------------------
# 6️⃣ Decorador personalizado (cronómetro)
# --------------------------------------------------
 
 
# --------------------------------------------------
# 7️⃣ Uso de map()
# --------------------------------------------------
 
 
# --------------------------------------------------
# 8️⃣ Uso de filter()
# --------------------------------------------------
 
 
# --------------------------------------------------
# 9️⃣ Uso de zip()
# --------------------------------------------------
 
 
# --------------------------------------------------
# 🔟 Uso de reduce()
# --------------------------------------------------
 
# ========================================
# Fin del Documento
# ========================================